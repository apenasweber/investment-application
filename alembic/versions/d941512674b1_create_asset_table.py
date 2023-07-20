"""create asset table

Revision ID: d941512674b1
Revises: bcca1e1497fa
Create Date: 2023-07-20 13:13:35.200046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d941512674b1"
down_revision = "bcca1e1497fa"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "asset",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("simbolo", sa.String(10), unique=True, nullable=False),
        sa.Column("preco_atual", sa.Float, nullable=False),
    )


def downgrade():
    op.drop_table("asset")
