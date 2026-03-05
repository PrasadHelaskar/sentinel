class Summarizer:

    @staticmethod
    def generate(report_summary, log_content):

        if isinstance(log_content, list):
            excerpt = "\n".join(log_content)
        else:
            excerpt = log_content

        if not excerpt:
            excerpt = "No anomalies detected in logs."

        return {
            "report": report_summary,
            "log_excerpt": excerpt
        }