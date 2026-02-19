from app.services.repo_monitor import RepoMonitor
from app.core.config import settings

def run():
    monitor = RepoMonitor(settings.REPOS, settings.ARTIFACT_NAME)
    monitor.process()

if __name__ == "__main__":
    run()