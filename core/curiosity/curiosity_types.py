from dataclasses import dataclass
from enum import Enum


class SignalType(Enum):
    UNCERTAINTY = "uncertainty"
    NOVELTY = "novelty"


@dataclass
class CuriositySignal:
    signal_type: SignalType
    value: float


@dataclass
class CuriosityScore:
    score: float
    signals: list[CuriositySignal]
