from dataclasses import dataclass
from enum import Enum


class ExperimentStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"


@dataclass
class ExperimentPlan:
    id: str
    hypothesis_id: str
    description: str
    metric_name: str


@dataclass
class ExperimentResult:
    experiment_id: str
    metric_value: float
    status: ExperimentStatus
