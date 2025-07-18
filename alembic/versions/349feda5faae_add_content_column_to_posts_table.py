"""add content column to posts table

Revision ID: 349feda5faae
Revises: 501bb67aee89
Create Date: 2025-07-12 22:28:14.599376

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '349feda5faae'
down_revision: Union[str, Sequence[str], None] = '501bb67aee89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')