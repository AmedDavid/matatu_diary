"""create tables

Revision ID: 411dcafe5e82
Revises: 
Create Date: 2025-05-28 08:55:05.486441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '411dcafe5e82'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('riders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('usual_stop', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('matatu_rides',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rider_id', sa.Integer(), nullable=False),
    sa.Column('route', sa.String(), nullable=False),
    sa.Column('fare', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('notes', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['rider_id'], ['riders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('matatu_rides')
    op.drop_table('riders')
    # ### end Alembic commands ###
