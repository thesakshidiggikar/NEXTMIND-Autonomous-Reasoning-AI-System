from dataclasses import dataclass
from enum import Enum


class MetaDecision(Enum):
    EXPLORE = "explore"
    EXPLOIT = "exploit"


@dataclass
class MetaAction:
    decision: MetaDecision
    reason: str
