from core.analysis.base import BaseResultAnalyzer
from core.analysis.analysis_types import AnalysisResult, AnalysisDecision


class SimpleResultAnalyzer(BaseResultAnalyzer):

    def analyze(self, hypothesis_id: str, metric_value: float) -> AnalysisResult:
        decision = (
            AnalysisDecision.ACCEPT
            if metric_value >= 0.6
            else AnalysisDecision.REJECT
        )

        confidence = min(max(metric_value, 0.0), 1.0)

        return AnalysisResult(
            hypothesis_id=hypothesis_id,
            decision=decision,
            confidence=confidence
        )
