from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, image
from sqlalchemy.orm import relationship

from .database import Base

class Card(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    job = Column(String)
    phone = Column(String)
    email = Column(String)
    address = Column(String)
    company = Column(String)
    # image = image_