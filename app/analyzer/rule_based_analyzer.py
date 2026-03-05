from app.analyzer.log_analyzer import LogAnalyzer
from app.analyzer.analysis_result import AnalysisResult


class RuleBasedAnalyzer(LogAnalyzer):

    KEYWORDS = ["FAILED", "AssertionError", "Exception", "ERROR", "Traceback"]

    def analyze(self, log_lines):

        result = AnalysisResult(
            failed_test=None,
            error_type=None,
            error_message=None,
            log_snippet=[]
        )

        for line in log_lines:

            if "FAILED" in line and result.failed_test is None:
                result.failed_test = line.strip()

            if any(k in line for k in self.KEYWORDS):

                if result.error_message is None:
                    result.error_message = line.strip()

                result.log_snippet.append(line.strip())

            if len(result.log_snippet) >= 5:
                break

        return result