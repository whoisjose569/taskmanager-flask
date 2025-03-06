from src.infra.repositories.task.task_repository import TaskRepository
from src.domain.task_use_cases.list_task_by_titly_use_case import ListTaskByTitleUseCase
from src.infra.services.task_services.list_task_service import ListTaskService


class ListTaskByTitleComposer:

    @staticmethod
    def list_task_composer() -> ListTaskService:
        task_repository = TaskRepository()
        list_task_use_case = ListTaskByTitleUseCase(task_repository)
        return ListTaskService(list_task_use_case)
