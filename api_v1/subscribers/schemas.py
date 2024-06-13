from pydantic import BaseModel, ConfigDict


class SubscriberBase(BaseModel):
    email: str


class SubscriberCreate(SubscriberBase):
    pass


class SubscriberUpdate(SubscriberCreate):
    pass


class Subscriber(SubscriberBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
