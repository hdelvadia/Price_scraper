"""third migration

Revision ID: 09bb07accc9b
Revises: c7bf4d772a42
Create Date: 2020-02-27 19:58:47.755768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09bb07accc9b'
down_revision = 'c7bf4d772a42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=64), nullable=True))
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.drop_column('user', 'email')
    # ### end Alembic commands ###
