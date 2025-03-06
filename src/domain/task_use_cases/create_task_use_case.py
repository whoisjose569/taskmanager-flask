from src.data.interfaces.task_repository_interface import TaskRepositoryInterface
from src.domain.interfaces.create_task_use_case_interface import (
    CreateTaskUseCaseInterface,
)
from src.domain.entities.task_entitie import TaskEntitie
from src.errors.custom_errors import TaskAlreadyExistsError


class CreateTaskUseCase(CreateTaskUseCaseInterface):
    def __init__(self, task_repository: TaskRepositoryInterface):
        self.__task_repository = task_repository

    def handle(self, task: dict) -> TaskEntitie:
        if self.__task_repository.list_task_by_title(task["title"]):
            raise TaskAlreadyExistsError()
        new_task = TaskEntitie(**task)
        return self.__task_repository.create_task(new_task)
