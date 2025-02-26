from flask import Blueprint, request
from http import HTTPStatus
from src.infra.repositories.task.task_repository import TaskRepository
from src.composers.task.create_task_composer import TaskComposer
from src.presenters.task_presenter import TaskPresenter

bp = Blueprint("task", __name__, url_prefix="/tasks")


@bp.route("/", methods=["POST"])
def create_task():
    try:
        task_repository = TaskRepository()

        data = request.json

        service = TaskComposer.create_task_composer(task_repository)

        response = service.handle(data)

        formatted_response = TaskPresenter.format_response(response)
        return formatted_response, HTTPStatus.CREATED
    except Exception as exc:
        raise
