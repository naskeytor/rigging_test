"""Add description col

Revision ID: 6c5b9f0c52be
Revises: 99c81b297b3f
Create Date: 2024-03-14 19:00:24.656398

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c5b9f0c52be'
down_revision = '99c81b297b3f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rigging', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('rigging', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
