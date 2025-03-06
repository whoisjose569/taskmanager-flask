from marshmallow import fields, validates
from src.data.models.task_model import TaskModel
from src.utils import ma


class CreateTaskSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TaskModel
        exclude = ("id",)

    title = fields.String(required=True)
    description = fields.String(load_default=None)
    status = fields.String(load_default="pending")
