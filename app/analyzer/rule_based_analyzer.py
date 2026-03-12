from app.analyzer.log_analyzer import LogAnalyzer
from app.analyzer.analysis_result import AnalysisResult


class RuleBasedAnalyzer(LogAnalyzer):

    KEYWORDS = [
        "failed",
        "assertionerror",
        "exception",
        "error",
        "traceback"
    ]

    def analyze(self, log_lines):

        result = AnalysisResult(
            failed_test=None,
            error_type=None,
            error_message=None,
            log_snippet=[]
        )

        print("Total log lines received:", len(log_lines))
        for line in log_lines:

            line_lower = line.lower()

            if "failed" in line_lower and result.failed_test is None:
                result.failed_test = line.strip()
                result.log_snippet.append(line.strip())

            if any(k in line_lower for k in self.KEYWORDS):

                if result.error_message is None:
                    result.error_message = line.strip()

                result.log_snippet.append(line.strip())

            if len(result.log_snippet) >= 5:
                break
                
        return result
        #https://www.workable.com/c/e9dc08f4-bd14-44d0-b7db-64ab90d1fd1f