from app.analyzer.log_analyzer import LogAnalyzer 
from app.analyzer.analysis_result import AnalysisResult

class RuleBasedAnalyzer(LogAnalyzer):

    def analyze(self, log_lines):

        if isinstance(log_lines, str):
            log_lines = log_lines.splitlines()
        
        result = AnalysisResult(
            failed_test=None,
            error_type=None,
            error_message=None,
            log_snippet=[]
        )

        for line in log_lines:
            line_lower = line.lower().strip()

            # Capture FAILED test clearly
            if "failed:" in line_lower and result.failed_test is None:
                result.failed_test = line.strip()
                result.log_snippet.append(line.strip())
                continue  # avoid double processing

            # Capture actual error message
            if "error -" in line_lower or "error:" in line_lower:

                # skip FAILED line already handled
                if "failed:" in line_lower:
                    continue

                if result.error_message is None:
                    result.error_message = line.strip()

                result.log_snippet.append(line.strip())

            # Capture traceback or exception explicitly
            if "traceback" in line_lower or "exception" in line_lower:
                result.log_snippet.append(line.strip())

            # Limit snippet AFTER meaningful capture
            if len(result.log_snippet) >= 5:
                break

        print("result:", result)
        return result