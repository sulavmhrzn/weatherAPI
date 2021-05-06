import os
import json
import fastapi
import uvicorn
from pathlib import Path
from starlette.staticfiles import StaticFiles
from views import home, weather_api
from services import get_weather

api = fastapi.FastAPI()
api.mount("/static", StaticFiles(directory="static"), name="static")
api.include_router(home.router)
api.include_router(weather_api.router)


def configure():
    configure_json()


def configure_json():
    json_path = Path("settings.json").absolute()
    if not os.path.exists(json_path):
        print("settings.json file was not found. The script will now terminate.")
        raise FileNotFoundError()
    with open("settings.json") as f:
        settings = json.load(f)
    get_weather.API_KEY = settings.get("API_KEY")


if __name__ == "__main__":
    configure()
    uvicorn.run(api)
else:
    configure()
