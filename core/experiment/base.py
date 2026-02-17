from abc import ABC, abstractmethod
from core.experiment.experiment_types import ExperimentResult, ExperimentPlan


class BaseExperimentRunner(ABC):

    @abstractmethod
    def run(self, plan: ExperimentPlan) -> ExperimentResult:
        pass
