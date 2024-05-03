from database import Base
from sqlalchemy import Column, Integer, String


class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=30))
    phone_number = Column(String(length=40))
    description = Column(String(length=200))
