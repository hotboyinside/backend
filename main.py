from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.models import ParticipantBase, SubscriberBase, db_helper
from api_v1 import router as router_v1


origins = [
    'http://localhost:5173',
    'http://83.166.238.188'
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(ParticipantBase.metadata.create_all)
        await conn.run_sync(SubscriberBase.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=router_v1, prefix="/api/v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get("/")
def hello_world():
    return 'Hello world!'
