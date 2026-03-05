import requests
import json

from app.core.config import settings
from utils.logger import Logger

log=Logger().get_logger(__name__)

class SlackNotifier:

    def __init__(self):
        self.webhook_url=settings.SLACK_WEBHOOK_URL

    def send_run_summary(self, data):
        
        report = data.get("report", {})  # extract nested report

        total = int(report.get("total", 0))
        passed = int(report.get("passed", 0))
        failed = int(report.get("failed", 0))
        skipped = int(report.get("skipped", 0))
        error = int(report.get("error", 0))

        # Determine status
        is_success = failed == 0 and error == 0
        status = "SUCCESS ✅" if is_success else "FAILED ❌"
        color = "#2eb886" if is_success else "#e01e5a"

        # Calculate pass rate
        pass_rate = f"{(passed / total * 100):.1f}%" if total > 0 else "0%"

        fields = [
            {"type": "mrkdwn", "text": f"*Repository*\n{data.get('repo')}"},
            {"type": "mrkdwn", "text": f"*Run ID*\n{data.get('run_id')}"},
            {"type": "mrkdwn", "text": f"*Total*\n{total}"},
            {"type": "mrkdwn", "text": f"*Passed*\n{passed}"},
        ]

        if failed > 0:
            fields.append({"type": "mrkdwn", "text": f"*Failed*\n{failed} ❌"})

        if error > 0:
            fields.append({"type": "mrkdwn", "text": f"*Errors*\n{error} ⚠"})

        if skipped > 0:
            fields.append({"type": "mrkdwn", "text": f"*Skipped*\n{skipped} ⏭"})

        fields.append({"type": "mrkdwn", "text": f"*Pass Rate*\n{pass_rate}"})

        payload = {
            "attachments": [
                {
                    "color": color,
                    "blocks": [
                        {
                            "type": "section",
                            "text": {
                                "type": "mrkdwn",
                                "text": f"🚀 *Test Run {status}*"
                            }
                        },
                        {
                            "type": "section",
                            "fields": fields
                            
                        }
                    ]
                }
            ]
        }

        response = requests.post(
            self.webhook_url,
            data=json.dumps(payload),
            headers={"Content-Type": "application/json"},
            timeout=10
        )

        if response.status_code != 200:
            raise Exception(f"Slack notification failed: {response.text}")