from abc import ABC, abstractmethod
from typing import List
from core.knowledge.knowledge_types import KnowledgeItem


class BaseKnowledgeStore(ABC):

    @abstractmethod
    def add(self, item: KnowledgeItem) -> None:
        pass

    @abstractmethod
    def get_all(self) -> List[KnowledgeItem]:
        pass
