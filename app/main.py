from app.services.repo_monitor import RepoMonitor
from app.core.config import settings
from utils.logger import Logger
from utils.cli_logger import CLILogger

def run():
    logger = Logger().get_logger("CLI")

    # Start CLI capture BEFORE pytest execution
    cli_logger = CLILogger(logger)
    cli_logger.start_capture()

    monitor = RepoMonitor(settings.REPOS, settings.ARTIFACT_NAME)
    monitor.process()

    # Optional (if you want restore)
    cli_logger.stop_capture()

if __name__ == "__main__":
    run()