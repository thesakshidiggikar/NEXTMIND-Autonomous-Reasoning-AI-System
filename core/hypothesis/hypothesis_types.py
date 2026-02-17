from dataclasses import dataclass
from enum import Enum


class HypothesisStatus(Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"


@dataclass
class Hypothesis:
    id: str
    description: str
    confidence: float
    status: HypothesisStatus = HypothesisStatus.PENDING
