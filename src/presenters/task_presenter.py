class TaskPresenter:
    @staticmethod
    def format_response(task):
        return {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "status": task.status,
            "created_at": task.created_at,
        }
