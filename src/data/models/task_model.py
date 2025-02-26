import sqlalchemy as sa
from src.utils import db
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(sa.String(255), nullable=False, index=True)
    description: Mapped[str] = mapped_column(sa.String(255), nullable=True)
    status: Mapped[str] = mapped_column(sa.String(50), default="pending")
    created_at: Mapped[datetime] = mapped_column(sa.DateTime, server_default=func.now())
