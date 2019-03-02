"""Initial Migration

Revision ID: e80f8cee31c1
Revises: e77838809d6c
Create Date: 2019-03-02 11:40:42.018115

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e80f8cee31c1'
down_revision = 'e77838809d6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('category', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
