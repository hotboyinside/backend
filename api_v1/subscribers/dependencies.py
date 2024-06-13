from typing import Annotated

from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Subscriber

from . import crud


async def subscriber_by_id(
        subscriber_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> Subscriber:
    subscriber = await crud.get_subscriber_by_id(subscriber_id=subscriber_id, session=session)
    if subscriber is not None:
        return subscriber

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Participant with {subscriber_id}id not found!"
    )
