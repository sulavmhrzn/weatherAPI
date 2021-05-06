from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):
    city: Optional[str] = None
    country: str = "nepal"
    units: str = "metric"
