from src.data.interfaces.task_repository_interface import TaskRepositoryInterface
from src.domain.interfaces.list_task_use_case_interface import ListTaskUseCaseInterface
from src.domain.entities.task_entitie import TaskEntitie
from src.errors.custom_errors import TaskNotExistsError


class ListTaskUseCase(ListTaskUseCaseInterface):
    def __init__(self, task_repository: TaskRepositoryInterface):
        self.__task_repository = task_repository

    def handle(self, task_title: str) -> TaskEntitie:
        task_on_db = self.__task_repository.list_task_by_title(task_title)
        if not task_on_db:
            raise TaskNotExistsError()
        return task_on_db
