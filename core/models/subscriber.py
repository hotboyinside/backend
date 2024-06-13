from sqlalchemy.orm import Mapped

from .base import SubscriberBase


class Subscriber(SubscriberBase):
    __tablename__ = "subscribers"

    email: Mapped[str]
