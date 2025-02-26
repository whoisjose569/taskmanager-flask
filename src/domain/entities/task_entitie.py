from datetime import datetime


class TaskEntitie:
    def __init__(
        self,
        title: str,
        description: str,
        status: str = "pending",
        create_at: datetime = None,
    ):
        self.title = title
        self.description = description
        self.status = status
        self.create_at = create_at

    def mark_as_done(self):
        self.status = "done"
