from dataclasses import dataclass
from enum import Enum


class KnowledgeStatus(Enum):
    SUCCESS = "success"
    FAILURE = "failure"


@dataclass
class KnowledgeItem:
    hypothesis_id: str
    decision: KnowledgeStatus
    confidence: float
