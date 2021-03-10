"""Add a column

Revision ID: 84aa5cc214fa
Revises: ccd38ad5fced
Create Date: 2021-03-08 17:21:55.593106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84aa5cc214fa'
down_revision = u'ccd38ad5fced'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('group', sa.Column('bi_report_id', sa.Text))
    op.add_column('group', sa.Column('bi_group_id', sa.Text))
    pass


def downgrade():
    op.drop_column('group', 'bi_report_id')
    op.drop_column('group', 'bi_group_id')
    pass
