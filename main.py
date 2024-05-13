from fastapi import FastAPI, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pydantic_extra_types.phone_numbers import PhoneNumber

from database import SessionLocal, engine

import models

app = FastAPI()

origins = [
    'http://localhost:5173',
    'http://83.166.238.188'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


class ParticipantBase(BaseModel):
    name: str
    phone_number: PhoneNumber
    description: str


class ParticipantModel(ParticipantBase):
    id: int

    class Config:
        from_attributes = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)


@app.post("/participants", response_model=ParticipantModel, status_code=201)
async def create_participant(participant: ParticipantBase, db: db_dependency):
    db_participant = models.Participant(**participant.dict())
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant
