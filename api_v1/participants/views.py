from typing import List

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .dependencies import participant_by_id
from .schemas import Participant, ParticipantCreate, ParticipantUpdate, ParticipantUpdatePartial
from core.models import db_helper

router = APIRouter(tags=["Participants"])


@router.get("/", response_model=List[Participant])
async def get_participants(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_participants(session=session)


@router.post("/", response_model=Participant, status_code=status.HTTP_201_CREATED)
async def create_participant(
        participant_in: ParticipantCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_participant(session=session, participant_in=participant_in)


@router.get("/{participant_id}/", response_model=Participant)
async def get_participant_by_id(
        participant: Participant = Depends(participant_by_id)
):
    return participant


@router.put("/{participant_id}/", response_model=Participant)
async def update_participant(
        participant_update: ParticipantUpdate,
        participant: Participant = Depends(participant_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_participant(
        session=session,
        participant=participant,
        participant_update=participant_update
    )


@router.patch("/{participant_id}/", response_model=Participant)
async def update_participant_partial(
        participant_update: ParticipantUpdatePartial,
        participant: Participant = Depends(participant_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_participant(
        session=session,
        participant=participant,
        participant_update=participant_update,
        partial=True
    )


@router.delete("/{participant_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_participant(
    participant: Participant = Depends(participant_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await crud.delete_participant(session=session, participant=participant)
