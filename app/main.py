from fastapi import FastAPI
from app.api.routes_health import router as health_router
from app.api.routes_booking import router as booking_router
from app.api.routes_talent import router as talent_router
from app.api.routes_storyline import router as storyline_router
from app.api.routes_collab import router as collab_router

app = FastAPI(
    title="FruitAI",
    description="AI-powered wrestling booking and event operations platform",
    version="0.1.0",
)

app.include_router(health_router, tags=["health"])
app.include_router(booking_router, prefix="/booking", tags=["booking"])
app.include_router(talent_router, prefix="/talent", tags=["talent"])
app.include_router(storyline_router, prefix="/storyline", tags=["storyline"])
app.include_router(collab_router, prefix="/collab", tags=["collaboration"])
