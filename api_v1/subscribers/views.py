from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .dependencies import subscriber_by_id
from .schemas import Subscriber, SubscriberCreate, SubscriberUpdate
from core.models import db_helper

router = APIRouter(tags=["Subscribers"])


@router.get("/", response_model=List[Subscriber])
async def get_subscribers(session: AsyncSession = Depends(db_helper.scoped_session_dependency)):
    return await crud.get_subscribers(session=session)


@router.post("/", response_model=Subscriber, status_code=status.HTTP_201_CREATED)
async def create_subscriber(
        subscriber_in: SubscriberCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.create_subscriber(session=session, subscriber_in=subscriber_in)


@router.get("/{subscriber_id}/", response_model=Subscriber)
async def get_subscriber_by_id(
        subscriber: Subscriber = Depends(subscriber_by_id)
):
    return subscriber


@router.put("/{subscriber_id}/", response_model=Subscriber)
async def update_subscriber(
        subscriber_update: SubscriberUpdate,
        subscriber: Subscriber = Depends(subscriber_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_subscriber(
        session=session,
        subscriber=subscriber,
        subscriber_update=subscriber_update
    )


@router.delete("/{subscriber_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_subscriber(
    subscriber: Subscriber = Depends(subscriber_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency)
) -> None:
    await crud.delete_subscriber(session=session, subscriber=subscriber)
