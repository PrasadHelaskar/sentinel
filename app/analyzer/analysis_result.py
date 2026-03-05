from dataclasses import dataclass
from typing import List, Optional


@dataclass
class AnalysisResult:
    failed_test: Optional[str] = None
    error_type: Optional[str] = None
    error_message: Optional[str] = None
    log_snippet: List[str] = None