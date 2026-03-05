import os
from app.github.client import GitHubClient
from app.analyzer.rule_based_analyzer import RuleBasedAnalyzer
from app.core.state_manager import StateManager
from app.services.artifact_service import ArtifactService
from app.services.report_parser import ReportParser
from app.services.log_parser import LogParser
from app.services.summarizer import Summarizer
from app.notifier.console_notifier import ConsoleNotifier
from app.notifier.slack_notifier import SlackNotifier
from utils.logger import Logger

log=Logger().get_logger(__name__)

class RepoMonitor:

    def __init__(self, repos, artifact_name):
        self.repos = repos
        self.artifact_name = artifact_name

    def process(self):
        github = GitHubClient()

        for repo in self.repos:
            runs = github.get_workflow_runs(repo)

            for run in runs[:3]:  # limit for safety
                run_id = run["id"]

                if StateManager.is_processed(repo, run_id):
                    continue

                artifacts = github.get_artifacts(repo, run_id)
                target = None

                for a in artifacts:
                    if a["name"] == self.artifact_name:
                        target=a
                        break
                    
                if not target:
                    continue

                content = github.download_artifact(repo, target["id"])
                extract_path = ArtifactService.extract_zip(content, f"artifacts/{repo}")

                report_path = os.path.join(extract_path, "reports", "report.html")

                report_summary = ReportParser.parse(report_path)
                raw_logs = LogParser.get_latest_log(extract_path)

                analysis = RuleBasedAnalyzer().analyze(raw_logs)

                log_content= analysis.log_snippet
                
                summary = Summarizer.generate(report_summary, log_content)
                
                ConsoleNotifier.notify({
                    "repo": repo,
                    "run_id": run_id,
                    **summary
                })

                SlackNotifier().send_run_summary({
                    "repo": repo,
                    "run_id": run_id,
                    **summary
                })

                StateManager.mark_processed(repo, run_id)