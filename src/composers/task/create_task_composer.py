from src.infra.repositories.task.task_repository import TaskRepository
from src.domain.task_use_cases.create_task_use_case import CreateTaskUseCase
from src.infra.services.task_services.create_task_service import CreateTaskService


class TaskComposer:

    @staticmethod
    def create_task_composer(task_repository: TaskRepository) -> CreateTaskService:
        create_task_use_case = CreateTaskUseCase(task_repository)
        return CreateTaskService(create_task_use_case)
