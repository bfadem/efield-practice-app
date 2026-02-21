from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Index
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone


db = SQLAlchemy()


class Attempt(db.Model):
    __tablename__ = "attempts"
    __table_args__ = (Index("ix_attempts_user_code", "user_code"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    user_code: Mapped[str] = mapped_column(db.String(64), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        db.DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    seed: Mapped[int] = mapped_column(db.Integer, nullable=False)
    config_json: Mapped[str] = mapped_column(db.Text, nullable=False)
    submitted_ex: Mapped[float] = mapped_column(db.Float, nullable=False)
    submitted_ey: Mapped[float] = mapped_column(db.Float, nullable=False)
    submitted_mag: Mapped[float] = mapped_column(db.Float, nullable=False)
    submitted_theta_deg: Mapped[float] = mapped_column(db.Float, nullable=False)
    correct_ex: Mapped[float] = mapped_column(db.Float, nullable=False)
    correct_ey: Mapped[float] = mapped_column(db.Float, nullable=False)
    correct_mag: Mapped[float] = mapped_column(db.Float, nullable=False)
    correct_theta_deg: Mapped[float] = mapped_column(db.Float, nullable=False)
    tol_percent: Mapped[float] = mapped_column(db.Float, nullable=False)
    tol_theta_deg: Mapped[float] = mapped_column(db.Float, nullable=False)
    ex_correct: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    ey_correct: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    mag_correct: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    theta_correct: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    score: Mapped[float] = mapped_column(db.Float, nullable=False)
