from typing import Annotated

from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Participant

from . import crud


async def participant_by_id(
        participant_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Participant:
    participant = await crud.get_participant_by_id(participant_id=participant_id, session=session)
    if participant is not None:
        return participant

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Participant with {participant_id}id not found!"
    )
