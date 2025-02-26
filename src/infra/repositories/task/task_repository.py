from src.data.interfaces.task_repository_interface import TaskRepositoryInterface
from src.data.models.task_model import TaskModel
from src.domain.entities.task_entitie import TaskEntitie
from src.utils import db


class TaskRepository(TaskRepositoryInterface):
    def __init__(self):
        self.__db_session = db.session

    def create_task(self, task: TaskEntitie):
        """Cria uma nova tarefa no banco de dados"""
        new_task = TaskModel(
            title=task.title,
            description=task.description,
            status=task.status,
            created_at=task.create_at,
        )
        self.__db_session.add(new_task)
        self.__db_session.commit()
        return new_task

    def list_task_by_title(self, title):
        """Busca uma tarefa no banco pelo titulo"""
        task_on_db = self.__db_session.query(TaskModel).filter_by(title=title).first()
        return task_on_db
