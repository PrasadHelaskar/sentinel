from bs4 import BeautifulSoup

class ReportParser:

    @staticmethod
    def parse(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        summary = {}

        # Basic extraction (adjust based on your pytest-html structure)
        stats = soup.find_all("span", class_="counter")

        if stats and len(stats) >= 3:
            summary["passed"] = stats[0].text
            summary["failed"] = stats[1].text
            summary["skipped"] = stats[2].text
        else:
            summary["info"] = "Unable to parse detailed stats"

        return summary
