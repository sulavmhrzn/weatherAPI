import os
import json
import fastapi
import uvicorn
from pathlib import Path
from starlette.staticfiles import StaticFiles
from views import home

api = fastapi.FastAPI()
api.include_router(home.router)
api.mount("/static", StaticFiles(directory="static"), name="static")


def configure():
    configure_json()


def configure_json():
    json_path = Path("settings.json").absolute()
    if not os.path.exists(json_path):
        print("settings.json file was not found. The script will now terminate.")
        raise FileNotFoundError()
    with open("settings.json") as f:
        settings = json.load(f)


if __name__ == "__main__":
    configure()
    uvicorn.run(api)
else:
    configure()
