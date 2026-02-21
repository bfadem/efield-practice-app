"""add magnitude and theta fields

Revision ID: 0002_add_mag_theta
Revises: 0001_create_attempts
Create Date: 2026-02-21 00:00:00
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0002_add_mag_theta"
down_revision: Union[str, None] = "0001_create_attempts"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "attempts",
        sa.Column("submitted_mag", sa.Float(), nullable=False, server_default=sa.text("0")),
    )
    op.add_column(
        "attempts",
        sa.Column("submitted_theta_deg", sa.Float(), nullable=False, server_default=sa.text("0")),
    )
    op.add_column(
        "attempts",
        sa.Column("correct_mag", sa.Float(), nullable=False, server_default=sa.text("0")),
    )
    op.add_column(
        "attempts",
        sa.Column("correct_theta_deg", sa.Float(), nullable=False, server_default=sa.text("0")),
    )
    op.add_column(
        "attempts",
        sa.Column("tol_theta_deg", sa.Float(), nullable=False, server_default=sa.text("0")),
    )
    op.add_column(
        "attempts",
        sa.Column("mag_correct", sa.Boolean(), nullable=False, server_default=sa.text("0")),
    )
    op.add_column(
        "attempts",
        sa.Column("theta_correct", sa.Boolean(), nullable=False, server_default=sa.text("0")),
    )


def downgrade() -> None:
    op.drop_column("attempts", "theta_correct")
    op.drop_column("attempts", "mag_correct")
    op.drop_column("attempts", "tol_theta_deg")
    op.drop_column("attempts", "correct_theta_deg")
    op.drop_column("attempts", "correct_mag")
    op.drop_column("attempts", "submitted_theta_deg")
    op.drop_column("attempts", "submitted_mag")
