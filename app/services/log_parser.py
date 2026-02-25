import os

class LogParser:

    @staticmethod
    def get_latest_log(base_path):
        reports_path = os.path.join(base_path, "reports")

        if not os.path.exists(reports_path):
            return None

        # ✅ Get only year directories
        years = sorted(
            [d for d in os.listdir(reports_path)
             if os.path.isdir(os.path.join(reports_path, d))],
            reverse=True
        )

        if not years:
            return None

        latest_year_path = os.path.join(reports_path, years[0])

        # ✅ Get only month directories
        months = sorted(
            [d for d in os.listdir(latest_year_path)
             if os.path.isdir(os.path.join(latest_year_path, d))],
            reverse=True
        )

        if not months:
            return None

        latest_month_path = os.path.join(latest_year_path, months[0])

        # ✅ Get only .log files
        log_files = sorted(
            [f for f in os.listdir(latest_month_path)
             if f.endswith(".log")],
            reverse=True
        )

        if not log_files:
            return None

        latest_log_path = os.path.join(latest_month_path, log_files[0])

        with open(latest_log_path, "r", encoding="utf-8") as f:
            return f.read()