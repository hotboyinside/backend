from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select

from core.models import Subscriber

from .schemas import SubscriberCreate, SubscriberUpdate


async def get_subscribers(session: AsyncSession) -> List[Subscriber]:
    request = select(Subscriber).order_by(Subscriber.id)
    result: Result = await session.execute(request)
    subscribers = result.scalars().all()
    return list(subscribers)


async def get_subscriber_by_id(session: AsyncSession, subscriber_id: int) -> Subscriber | None:
    return await session.get(Subscriber, subscriber_id)


async def create_subscriber(session: AsyncSession, subscriber_in: SubscriberCreate) -> Subscriber:
    subscriber = Subscriber(**subscriber_in.model_dump())
    session.add(subscriber)
    await session.commit()
    await session.refresh(subscriber)
    return subscriber


async def update_subscriber(
    session: AsyncSession,
    subscriber: Subscriber,
    subscriber_update: SubscriberUpdate
) -> Subscriber:
    for name, value in subscriber_update.model_dump().items():
        setattr(subscriber, name, value)
    await session.commit()
    return subscriber


async def delete_subscriber(
    session: AsyncSession,
    subscriber: Subscriber,
) -> None:
    await session.delete(subscriber)
    await session.commit()
