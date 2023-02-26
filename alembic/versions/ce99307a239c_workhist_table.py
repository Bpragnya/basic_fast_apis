"""workhist table

Revision ID: ce99307a239c
Revises: e45cd19d0cb6
Create Date: 2023-02-16 19:22:05.858387

"""
from alembic import op
from sqlalchemy import INTEGER, VARCHAR, Column, Boolean, DateTime, func


# revision identifiers, used by Alembic.
revision = 'ce99307a239c'
down_revision = 'e45cd19d0cb6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "workhist",
        Column('id',INTEGER, primary_key=True, autoincrement=True),
        Column('comp_name',VARCHAR, nullable=False),
        Column('from_dt',DateTime),
        Column('to_dt',DateTime),
        Column('role', VARCHAR, nullable=False),
        Column('desc', VARCHAR),
        Column('is_active',Boolean, default=True),
        Column('emp_id',INTEGER),
        #Column('emp_id',INTEGER, ForeignKey('employees.id')),
        op.create_foreign_key(
            "fk_emp_id", "workhist",
            "employees", ["emp_id"], ["id"])
            
    )


def downgrade():
    op.drop_table('workhist')