"""create user_assets table

Revision ID: 69cf5a7da1d7
Revises: d941512674b1
Create Date: 2023-07-20 13:13:38.833876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "69cf5a7da1d7"
down_revision = "d941512674b1"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user_assets",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("user.id")),
        sa.Column("asset_id", sa.Integer, sa.ForeignKey("asset.id")),
        sa.Column("quantidade", sa.Integer, nullable=False),
    )


def downgrade():
    op.drop_table("user_assets")
