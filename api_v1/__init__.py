from fastapi import APIRouter
from .participants.views import router as participant_router
from .subscribers.views import router as subscriber_router

router = APIRouter()
router.include_router(router=participant_router, prefix='/participants')
router.include_router(router=subscriber_router, prefix='/subscribers')
