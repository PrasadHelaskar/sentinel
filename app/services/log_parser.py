import os

class LogParser:

    @staticmethod
    def get_latest_log(base_path):
        logs_path = os.path.join(base_path, "reports", "logs")
        if not os.path.exists(logs_path):
            return None

        days = sorted(os.listdir(logs_path), reverse=True)
        if not days:
            return None

        latest_day_path = os.path.join(logs_path, days[0])
        files = os.listdir(latest_day_path)

        if not files:
            return None

        log_file = os.path.join(latest_day_path, files[0])

        with open(log_file, "r", encoding="utf-8") as f:
            return f.read()
