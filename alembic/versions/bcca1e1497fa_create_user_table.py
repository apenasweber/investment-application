"""create user table

Revision ID: bcca1e1497fa
Revises: 
Create Date: 2023-07-20 13:13:28.389885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bcca1e1497fa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("cpf", sa.String(11), unique=True, nullable=False),
        sa.Column("nome", sa.String(100), nullable=False),
        sa.Column("saldo_em_conta", sa.Float, default=0),
        sa.Column("senha", sa.String(100), nullable=False),
        sa.Column("codigo_da_conta", sa.String(50), nullable=False),
        sa.Column("email", sa.String(100), nullable=False),
    )


def downgrade():
    op.drop_table("user")
