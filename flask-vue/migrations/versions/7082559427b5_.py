"""empty message

Revision ID: 7082559427b5
Revises: 
Create Date: 2017-03-01 12:28:21.882943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7082559427b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.Column('title', sa.Unicode(length=100), nullable=True),
    sa.Column('slug', sa.Unicode(length=100), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('html', sa.Text(), nullable=True),
    sa.Column('tags', sa.Unicode(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_tags'), 'posts', ['tags'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_tags'), table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###