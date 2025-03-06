from flask import json
from werkzeug.exceptions import HTTPException
from src.errors.custom_errors import *


def register_error_handlers(app):

    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        response = e.get_response()
        response.data = json.dumps(
            {
                "code": e.code,
                "name": e.name,
                "description": e.description,
            }
        )
        response.content_type = "application/json"
        return response

    @app.errorhandler(TaskAlreadyExistsError)
    def handle_task_already_exists_error(e):
        return {
            "code": 409,
            "name": "Conflict",
            "description": str(e),
        }, 409

    @app.errorhandler(TaskAlreadyExistsError)
    def handle_task_not_exists_error(e):
        return {
            "code": 404,
            "name": "NotFound",
            "description": str(e),
        }, 404

    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        return {
            "code": 500,
            "name": "Internal Server Error",
            "description": "Something Went Wrong on the Server.",
        }, 500
