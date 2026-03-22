class Summarizer:

    @staticmethod
    def generate(report_summary, analysis_result):

        if isinstance(analysis_result.log_snippet,list):
            excerpt = "\n".join(analysis_result.log_snippet)
        else:
            excerpt = analysis_result.log_snippet

        if not excerpt and analysis_result.failed_test:
            excerpt = analysis_result.failed_test

        if not excerpt:
            excerpt = "No anomalies detected in logs."

        return {
            "report": report_summary,
            "log_excerpt": excerpt
        }