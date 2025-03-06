from src.infra.repositories.task.task_repository import TaskRepository
from src.domain.task_use_cases.list_task_use_case import ListTaskUseCase
from src.infra.services.task_services.list_task_service import ListTaskService


class ListTaskComposer:

    @staticmethod
    def list_task_composer() -> ListTaskService:
        task_repository = TaskRepository()
        list_task_use_case = ListTaskUseCase(task_repository)
        return ListTaskService(list_task_use_case)
