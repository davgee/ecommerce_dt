import uuid

from sqlalchemy import Column, Integer, String, ForeignKeyConstraint, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:testpass@localhost:5433/db_ecommerce_data_trace', echo = True)
Base = declarative_base()


class Cart(Base):
    __tablename__ = "cart"

    id = Column(UUID, primary_key=True, nullable=False, default=uuid.uuid4)


class Item(Base):
    __tablename__ = "item"

    id = Column(UUID, primary_key=True, nullable=False, default=uuid.uuid4)
    cart_id = Column(UUID, ForeignKey('cart.id'))
    external_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)


Base.metadata.create_all(engine)
