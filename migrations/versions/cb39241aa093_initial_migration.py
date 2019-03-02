"""Initial Migration

Revision ID: cb39241aa093
Revises: d12fa71b496f
Create Date: 2019-03-02 12:59:06.790081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb39241aa093'
down_revision = 'd12fa71b496f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('username', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'username')
    # ### end Alembic commands ###
