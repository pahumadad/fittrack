"""add measurements sessions table

Revision ID: 1259609f4cfb
Revises: 2b8cb090c298
Create Date: 2018-03-11 19:21:18.027442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1259609f4cfb'
down_revision = '2b8cb090c298'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('measurements_sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('measurements_sessions')
    # ### end Alembic commands ###
