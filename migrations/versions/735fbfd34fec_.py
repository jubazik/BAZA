"""empty message

Revision ID: 735fbfd34fec
Revises: 
Create Date: 2022-07-06 14:06:31.838299

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '735fbfd34fec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('name_card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('room', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('room')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('name_card')
    # ### end Alembic commands ###
