from abc import ABC, abstractmethod
from src.domain.entities.task_entitie import TaskEntitie


class TaskRepositoryInterface(ABC):
    """Interface para repositórios de tarefas"""

    @abstractmethod
    def create_task(self, task) -> TaskEntitie:
        """Cria uma nova tarefa no banco de dados"""
        pass

    @abstractmethod
    def list_task_by_title(self, title) -> TaskEntitie:
        """Busca uma tarefa no banco pelo titulo"""
        pass
