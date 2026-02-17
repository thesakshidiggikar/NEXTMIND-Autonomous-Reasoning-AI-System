from abc import ABC, abstractmethod
from core.meta.meta_types import MetaAction


class BaseMetaController(ABC):

    @abstractmethod
    def decide(self, curiosity_score: float, success_rate: float) -> MetaAction:
        pass
