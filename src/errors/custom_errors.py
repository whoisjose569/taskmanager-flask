class TaskError(Exception):
    pass


class TaskAlreadyExistsError(TaskError):
    def __init__(self):
        super().__init__(f"Task with this title already exists")


class TaskNotExistsError(TaskError):
    def __init__(self):
        super().__init__(f"Task with this title Not exists")
