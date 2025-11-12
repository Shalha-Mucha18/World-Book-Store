"""make user first/last name nullable

Revision ID: 7b5a8d76a5c1
Revises: 1cd339a20c59
Create Date: 2025-11-12 11:00:00.000000
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7b5a8d76a5c1"
down_revision = "1cd339a20c59"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        "users",
        "first_name",
        existing_type=sa.String(),
        nullable=True,
    )
    op.alter_column(
        "users",
        "last_name",
        existing_type=sa.String(),
        nullable=True,
    )


def downgrade() -> None:
    op.alter_column(
        "users",
        "last_name",
        existing_type=sa.String(),
        nullable=False,
    )
    op.alter_column(
        "users",
        "first_name",
        existing_type=sa.String(),
        nullable=False,
    )
