"""followers

Revision ID: 4beea0e90911
Revises: 5242c9aa7584
Create Date: 2018-09-06 14:47:22.413842

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4beea0e90911'
down_revision = '5242c9aa7584'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
