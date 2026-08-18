from sqlalchemy import Column, Integer, String
from app.database import Base

#Creating DB model
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    quantity = Column(Integer, nullable=False)