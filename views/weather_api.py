from fastapi import APIRouter, Depends
from models.location import Location
from services.get_weather import get_weather

router = APIRouter()


@router.get("/api/weather")
def weather(loc: Location = Depends()):
    data = get_weather(**loc.dict())
    return data
