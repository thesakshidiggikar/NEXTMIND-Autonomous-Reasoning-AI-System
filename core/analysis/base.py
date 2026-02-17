from abc import ABC, abstractmethod
from core.analysis.analysis_types import AnalysisResult


class BaseResultAnalyzer(ABC):

    @abstractmethod
    def analyze(self, hypothesis_id: str, metric_value: float) -> AnalysisResult:
        pass
