from src.domain.task_use_cases.list_task_by_titly_use_case import ListTaskByTitleUseCase


class ListTaskService:
    def __init__(self, task_use_case: ListTaskByTitleUseCase):
        self.__task_use_case = task_use_case

    def handle(self, task_title):
        return self.__task_use_case.handle(task_title)
