from pydantic import BaseModel, ConfigDict

from pydantic_extra_types.phone_numbers import PhoneNumber


class ParticipantBase(BaseModel):
    name: str
    phone_number: PhoneNumber
    description: str


class ParticipantCreate(ParticipantBase):
    pass


class ParticipantUpdate(ParticipantCreate):
    pass


class ParticipantUpdatePartial(ParticipantCreate):
    name: str | None = None
    phone_number: PhoneNumber | None = None
    description: str | None = None


class Participant(ParticipantBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
