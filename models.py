from database import Base
from sqlalchemy import Boolean, Column, Integer, String, Text


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=True, unique=True)
    description = Column(Text)
    price = Column(Integer)
    on_offer = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Item: name={self.name} price={self.price}>"
