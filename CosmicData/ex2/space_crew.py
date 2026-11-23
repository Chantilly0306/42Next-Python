#!/usr/bin/env python3
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')

        if not any(
            member.rank in (Rank.CAPTAIN, Rank.COMMANDER)
            for member in self.crew):
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            veteran = sum(member.years_experience >= 5 for member in self.crew)
            if veteran < len(self.crew) / 2:
                raise ValueError("Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)")

        if self.

        return self