import uuid

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Cart(Base):
    __tablename__ = "cart"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, unique=True, nullable=False)


class Item(Base):
    __tablename__ = "item"

    id = Column(UUID(as_uuid=True), primary_key=True,
                default=uuid.uuid4, unique=True, nullable=False)
    cart_id = Column(UUID, ForeignKey('cart.id'))
    external_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
