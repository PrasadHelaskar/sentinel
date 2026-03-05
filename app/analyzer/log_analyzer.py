from abc import ABC, abstractmethod
from app.analyzer.analysis_result import AnalysisResult


class LogAnalyzer(ABC):

    @abstractmethod
    def analyze(self, log_lines) -> AnalysisResult:
        pass