from flask import Blueprint, request
from http import HTTPStatus
from src.presentation.schemas.task_schema import CreateTaskSchema
from src.composers.task.create_task_composer import TaskComposer
from src.composers.task.list_task_by_title_composer import ListTaskByTitleComposer
from src.presenters.task_presenter import TaskPresenter

bp = Blueprint("task", __name__, url_prefix="/tasks")


@bp.route("/", methods=["POST"])
def create_task():
    try:
        data = request.json
        schema = CreateTaskSchema()

        validated_data = schema.load(data)

        service = TaskComposer.create_task_composer()

        response = service.handle(validated_data)

        formatted_response = TaskPresenter.format_response(response)
        return formatted_response, HTTPStatus.CREATED
    except Exception as exc:
        raise


@bp.route("/", methods=["GET"])
def list_task_by_title():
    try:
        data = request.json

        service = ListTaskByTitleComposer.list_task_composer()

        response = service.handle(data)

        formatted_response = TaskPresenter.format_response(response)
        return formatted_response, HTTPStatus.CREATED
    except Exception as exc:
        raise
