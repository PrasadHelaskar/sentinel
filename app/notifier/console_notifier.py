class ConsoleNotifier:

    @staticmethod
    def notify(summary):
        print("\n====== SENTINEL REPORT ======")
        print("Report Stats:", summary["report"])
        print("\nLog Preview:\n", summary["log_excerpt"])
        print("================================\n")
