"""empty message

Revision ID: 721de78ea389
Revises: 8f7e62258d22
Create Date: 2021-05-16 06:52:45.663919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '721de78ea389'
down_revision = '8f7e62258d22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    # ### end Alembic commands ###