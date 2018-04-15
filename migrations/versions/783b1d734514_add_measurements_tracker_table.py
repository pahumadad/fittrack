"""add measurements_tracker table

Revision ID: 783b1d734514
Revises: 1259609f4cfb
Create Date: 2018-04-15 12:35:31.752704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '783b1d734514'
down_revision = '1259609f4cfb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('measurements_tracker',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('session', sa.Integer(), nullable=False),
    sa.Column('measurement', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('conclusion', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['measurement'], ['measurements.id'], ),
    sa.ForeignKeyConstraint(['session'], ['measurements_sessions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('measurements_tracker')
    # ### end Alembic commands ###
