#!/usr/bin/env python3
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def validate(data: dict):
    try:
        station = SpaceStation(**data)
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        print(
            "Status: ",
            "Operational" if station.is_operational else "Inoperative"
        )
    except ValidationError as e:
        print(e)


def main():
    print("Space Station Data Validation")
    print("========================================")

    station_data = {
        "station_id": "ISS754",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2024-01-15T10:30:00"
    }
    validate(station_data)

    print("\n========================================")
    station_data["crew_size"] = 21
    validate(station_data)


if __name__ == "__main__":
    main()
