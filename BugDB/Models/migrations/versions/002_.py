"""bug_header table init

Revision ID: 002
Revises: 001
Create Date: 2019-09-13 02:49:53.434683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bug_header',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=254), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('assigned_to_user_id', sa.Integer(), nullable=True),
    sa.Column('customer', sa.String(length=10), nullable=True),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.Column('priority', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['assigned_to_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bug_header')
    # ### end Alembic commands ###
