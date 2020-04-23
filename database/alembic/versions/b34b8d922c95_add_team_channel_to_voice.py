"""Add team channel to Voice

Revision ID: b34b8d922c95
Revises: f22b055b001e
Create Date: 2020-04-22 19:22:36.783640

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b34b8d922c95'
down_revision = 'f22b055b001e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('voice', sa.Column('is_team_channel', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('voice', 'is_team_channel')
    # ### end Alembic commands ###