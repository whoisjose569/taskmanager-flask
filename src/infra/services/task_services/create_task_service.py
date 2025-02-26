from src.domain.task_use_cases.create_task_use_case import CreateTaskUseCase


class CreateTaskService:
    def __init__(self, task_use_case: CreateTaskUseCase):
        self.__task_use_case = task_use_case

    def handle(self, task):
        return self.__task_use_case.handle(task)
