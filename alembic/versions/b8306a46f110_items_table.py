"""items_table

Revision ID: b8306a46f110
Revises: ce99307a239c
Create Date: 2023-02-28 16:52:14.103186

"""
from alembic import op
from sqlalchemy import INTEGER, VARCHAR, Column, ForeignKey


# revision identifiers, used by Alembic.
revision = 'b8306a46f110'
down_revision = 'ce99307a239c'
branch_labels = None
depends_on = None


def upgrade():
     op.create_table(
        "items",
        Column('id',INTEGER, primary_key=True, autoincrement=True),
        Column('title',VARCHAR),
        Column('description',VARCHAR),
        # Column('owner_id', INTEGER),
        Column('owner_id',INTEGER, ForeignKey('users.id')),
        # op.create_foreign_key(
        #     "fk_owner_id", "items",
        #     "users", ["owner_id"], ["id"])
    )


def downgrade():
    op.drop_table('items')