from dataclasses import dataclass
from enum import Enum


class AnalysisDecision(Enum):
    ACCEPT = "accept"
    REJECT = "reject"


@dataclass
class AnalysisResult:
    hypothesis_id: str
    decision: AnalysisDecision
    confidence: float
