"""Initial Migration

Revision ID: 504b9575e73c
Revises: 4f5bd8c88934
Create Date: 2019-03-04 17:05:52.889460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '504b9575e73c'
down_revision = '4f5bd8c88934'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'pic_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('pic_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###