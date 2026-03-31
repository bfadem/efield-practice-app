"""add force magnitude and direction fields

Revision ID: 0003_add_force_fields
Revises: 0002_add_mag_theta
Create Date: 2026-03-31 00:00:00
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "0003_add_force_fields"
down_revision: Union[str, None] = "0002_add_mag_theta"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "attempts",
        sa.Column("submitted_force_mag", sa.Float(), nullable=False, server_default=sa.text("0")),
    )
    op.add_column(
        "attempts",
        sa.Column("submitted_force_dir", sa.String(16), nullable=False, server_default=sa.text("'parallel'")),
    )
    op.add_column(
        "attempts",
        sa.Column("correct_force_mag", sa.Float(), nullable=False, server_default=sa.text("0")),
    )
    op.add_column(
        "attempts",
        sa.Column("correct_force_dir", sa.String(16), nullable=False, server_default=sa.text("'parallel'")),
    )
    op.add_column(
        "attempts",
        sa.Column("force_mag_correct", sa.Boolean(), nullable=False, server_default=sa.text("false")),
    )
    op.add_column(
        "attempts",
        sa.Column("force_dir_correct", sa.Boolean(), nullable=False, server_default=sa.text("false")),
    )


def downgrade() -> None:
    op.drop_column("attempts", "force_dir_correct")
    op.drop_column("attempts", "force_mag_correct")
    op.drop_column("attempts", "correct_force_dir")
    op.drop_column("attempts", "correct_force_mag")
    op.drop_column("attempts", "submitted_force_dir")
    op.drop_column("attempts", "submitted_force_mag")
