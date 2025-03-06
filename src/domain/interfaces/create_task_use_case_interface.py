from abc import ABC, abstractmethod
from typing import Dict
from src.domain.entities.task_entitie import TaskEntitie


class CreateTaskUseCaseInterface(ABC):
    @abstractmethod
    def handle(self, task: Dict) -> TaskEntitie:
        pass
