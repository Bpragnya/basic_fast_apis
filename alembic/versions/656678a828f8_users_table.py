"""users table

Revision ID: 656678a828f8
Revises: 
Create Date: 2023-02-16 16:17:32.306754

"""
from alembic import op
from sqlalchemy import INTEGER, VARCHAR, Column, Boolean, DateTime, func


# revision identifiers, used by Alembic.
revision = '656678a828f8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        Column('id',INTEGER, primary_key=True, autoincrement=True),
        Column('email',VARCHAR, unique=True, nullable=False),
        Column('password', VARCHAR),
        Column('timestamp', DateTime, server_default=func.now()),
        Column('is_active',Boolean, default=True)
    )


def downgrade():
    op.drop_table('users')

def populatedata():
    op.bulk_insert("users",
    [
        {'email':'me@gmail.com',
                'password':'me'},
        {'email':'you@gmail.com',
                'password':'you'},
    ]
)
