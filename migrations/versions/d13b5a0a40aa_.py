"""empty message

Revision ID: d13b5a0a40aa
Revises: 6c3b332b06ee
Create Date: 2023-04-07 02:03:30.998328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd13b5a0a40aa'
down_revision = '6c3b332b06ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.alter_column('desc',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=180),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('movies', schema=None) as batch_op:
        batch_op.alter_column('desc',
               existing_type=sa.String(length=180),
               type_=sa.VARCHAR(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###
