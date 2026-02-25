from utils.logger import Logger

log=Logger().get_logger(__name__)

class ConsoleNotifier:

    @staticmethod
    def notify(summary):
        log.info("====== SENTINEL REPORT ======\n")
        log.info("Report Stats: %s", summary["report"])
        log.info("Log Preview: %s", summary["log_excerpt"])
        log.info("================================\n")
