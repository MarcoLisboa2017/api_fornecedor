"""Adicionar campo estoque_atual à tabela estoques

Revision ID: 2d791f5350d3
Revises: 
Create Date: 2024-09-15 21:09:45.457665

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d791f5350d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('estoques', schema=None) as batch_op:
        batch_op.add_column(sa.Column('estoque_atual', sa.Float(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('estoques', schema=None) as batch_op:
        batch_op.drop_column('estoque_atual')

    # ### end Alembic commands ###
