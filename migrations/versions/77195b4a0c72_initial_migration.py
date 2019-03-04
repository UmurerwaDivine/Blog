"""Initial Migration

Revision ID: 77195b4a0c72
Revises: 975e534ecdbc
Create Date: 2019-03-04 08:33:40.911687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77195b4a0c72'
down_revision = '975e534ecdbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'pic_path')
    # ### end Alembic commands ###
