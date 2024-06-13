from sqlalchemy.orm import Mapped

from .base import ParticipantBase


class Participant(ParticipantBase):
    __tablename__ = "participants"

    name: Mapped[str]
    phone_number: Mapped[str]
    description: Mapped[str]
