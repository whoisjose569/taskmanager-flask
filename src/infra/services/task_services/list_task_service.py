from src.domain.task_use_cases.list_task_use_case import ListTaskUseCase


class ListTaskService:
    def __init__(self, task_use_case: ListTaskUseCase):
        self.__task_use_case = task_use_case

    def handle(self, data: dict):
        task_title = data["title"]
        return self.__task_use_case.handle(task_title)
