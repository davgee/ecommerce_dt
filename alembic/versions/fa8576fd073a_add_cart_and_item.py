"""Add cart and item

Revision ID: fa8576fd073a
Revises: 
Create Date: 2021-06-20 19:50:26.361999

"""
import uuid

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.

revision = "fa8576fd073a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "cart",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    )

    op.create_table(
        "item",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False),
        sa.Column("cart_id", UUID, sa.ForeignKey('cart.id')),
        sa.Column("external_id", sa.String, nullable=False),
        sa.Column("name", sa.String),
        sa.Column("value", sa.Integer)
    )


def downgrade():
    op.drop_table("item")
    op.drop_table("cart")
