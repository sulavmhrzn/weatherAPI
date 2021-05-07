from os import stat
from models.exce import ValidationError
from fastapi import APIRouter, Depends, responses
from models.location import Location
from services.get_weather import get_weather

router = APIRouter()


@router.get("/api/weather")
async def weather(loc: Location = Depends()):
    try:
        data = await get_weather(**loc.dict())
        return data
    except ValidationError as err:
        return responses.JSONResponse(
            content={"code": err.status_code, "message": err.message}, status_code=404
        )
