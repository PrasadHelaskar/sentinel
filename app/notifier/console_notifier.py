from utils.logger import Logger

log=Logger().get_logger(__name__)

class ConsoleNotifier:

    @staticmethod
    def notify(summary):
        log.info("====== SENTINEL REPORT ======\n")

        log.info("Repository: %s", summary["repo"])
        log.info("Run ID: %s\n", summary["run_id"])

        log.info("Report Summary: %s",summary["report"])

        log.info("Log Intelligence:\n %s",summary["log_excerpt"])

        log.info("Sentinel 🛡️ Guarding your pipelines.")
        log.info("================================\n")