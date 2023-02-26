"""employees table

Revision ID: e45cd19d0cb6
Revises: 656678a828f8
Create Date: 2023-02-16 19:19:14.400968

"""
from alembic import op
from sqlalchemy import INTEGER, VARCHAR, Column, Boolean, DateTime, func


# revision identifiers, used by Alembic.
revision = 'e45cd19d0cb6'
down_revision = '656678a828f8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "employees",
        Column('id',INTEGER, primary_key=True, autoincrement=True),
        Column('name',VARCHAR, nullable=False),
        Column('email',VARCHAR, unique=True, nullable=False),
        Column('city', VARCHAR),
        Column('state', VARCHAR),
        Column('pincode', INTEGER),
        Column('is_active',Boolean, default=True)
    )


def downgrade():
    op.drop_table('employees')
