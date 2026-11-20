#!/usr/bin/env python3
from datetime import datetime
from pydantic import BaseModel, Field


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


station_data = {
    "station_id": "ISS754",
    "name": "International Space Station",
    "crew_size": 6,
    "power_level": 85.5,
    "oxygen_level": 95.0,
    "last_maintenance": "2024-01-15T10:30:00"
}

station = SpaceStation(**station_data)
print(type(station))