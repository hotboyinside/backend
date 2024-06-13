from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select

from core.models import Participant

from .schemas import ParticipantCreate, ParticipantUpdate, ParticipantUpdatePartial


async def get_participants(session: AsyncSession) -> List[Participant]:
    request = select(Participant).order_by(Participant.id)
    result: Result = await session.execute(request)
    participants = result.scalars().all()
    return list(participants)


async def get_participant_by_id(session: AsyncSession, participant_id: int) -> Participant | None:
    return await session.get(Participant, participant_id)


async def create_participant(session: AsyncSession, participant_in: ParticipantCreate) -> Participant:
    participant = Participant(**participant_in.model_dump())
    session.add(participant)
    await session.commit()
    await session.refresh(participant)
    return participant


async def update_participant(
    session: AsyncSession,
    participant: Participant,
    participant_update: ParticipantUpdate | ParticipantUpdatePartial,
    partial: bool = False
) -> Participant:
    for name, value in participant_update.model_dump(exclude_unset=partial).items():
        setattr(participant, name, value)
    await session.commit()
    return participant


async def delete_participant(
    session: AsyncSession,
    participant: Participant,
) -> None:
    await session.delete(participant)
    await session.commit()
