class Summarizer:

    @staticmethod
    def generate(report_summary, log_content):
        return {
            "report": report_summary,
            "log_excerpt": log_content[:500] if log_content else "No logs found"
        }
