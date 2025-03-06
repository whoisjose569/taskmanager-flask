from abc import ABC, abstractmethod
from typing import Dict
from src.domain.entities.task_entitie import TaskEntitie


class ListTaskByTitleUseCaseInterface(ABC):
    @abstractmethod
    def handle(self, task_title: str) -> TaskEntitie:
        pass
