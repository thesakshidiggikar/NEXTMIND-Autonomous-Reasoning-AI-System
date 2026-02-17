from abc import ABC, abstractmethod
from core.curiosity.curiosity_types import CuriosityScore


class BaseCuriosityEngine(ABC):

    @abstractmethod
    def compute_curiosity(self, context: dict) -> CuriosityScore:
        pass
