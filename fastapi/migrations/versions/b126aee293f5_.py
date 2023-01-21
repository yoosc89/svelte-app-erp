"""empty message

Revision ID: b126aee293f5
Revises: 627009649a3e
Create Date: 2022-11-17 23:24:13.687418

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b126aee293f5'
down_revision = '627009649a3e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'modify_date',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'modify_date',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###
