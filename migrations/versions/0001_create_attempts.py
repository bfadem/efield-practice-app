"""create attempts table

Revision ID: 0001_create_attempts
Revises: 
Create Date: 2026-02-19 00:00:00
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0001_create_attempts"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "attempts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_code", sa.String(length=64), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("seed", sa.Integer(), nullable=False),
        sa.Column("config_json", sa.Text(), nullable=False),
        sa.Column("submitted_ex", sa.Float(), nullable=False),
        sa.Column("submitted_ey", sa.Float(), nullable=False),
        sa.Column("correct_ex", sa.Float(), nullable=False),
        sa.Column("correct_ey", sa.Float(), nullable=False),
        sa.Column("tol_percent", sa.Float(), nullable=False),
        sa.Column("ex_correct", sa.Boolean(), nullable=False),
        sa.Column("ey_correct", sa.Boolean(), nullable=False),
        sa.Column("score", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_attempts_user_code", "attempts", ["user_code"])


def downgrade() -> None:
    op.drop_index("ix_attempts_user_code", table_name="attempts")
    op.drop_table("attempts")
