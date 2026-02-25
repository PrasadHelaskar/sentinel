from bs4 import BeautifulSoup
import json

class ReportParser:

    @staticmethod
    def parse(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        summary = {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "skipped": 0,
            "error": 0,
        }

        data_container = soup.find("div", id="data-container")

        if not data_container or "data-jsonblob" not in data_container.attrs:
            summary["info"] = "Unable to locate pytest-html JSON data"
            return summary

        try:
            data = json.loads(data_container["data-jsonblob"])
        except json.JSONDecodeError:
            summary["info"] = "Invalid JSON in report"
            return summary

        tests = data.get("tests", {})

        for test_name, executions in tests.items():
            for test in executions:
                summary["total"] += 1
                result = test.get("result", "").lower()

                if result == "passed":
                    summary["passed"] += 1
                elif result == "failed":
                    summary["failed"] += 1
                elif result == "skipped":
                    summary["skipped"] += 1
                elif result == "error":
                    summary["error"] += 1

        return summary