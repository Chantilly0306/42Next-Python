#!/usr/bin/env python3
from enum import Enum
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_contact(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError('Contact ID must start with "AC"')

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")

        return self


def validate(data: dict):
    try:
        ac = AlienContact(**data)
        print("Valid contact report:")
        print(f"ID: {ac.contact_id}")
        print(f"Type: {ac.contact_type.value}")
        print(f"Location: {ac.location}")
        print(f"Signal: {ac.signal_strength}/10")
        print(f"Duration: {ac.duration_minutes} minutes")
        print(f"Witnesses: {ac.witness_count}")
        print(f"Message: '{ac.message_received}'")
    except ValidationError as e:
        print("Expected validation error:")
        print(e)


def main():
    data = {
        "contact_id": "AC_2024_001",
        "timestamp": datetime(2024, 1, 1, 1, 42, 42),
        "location": "Area 51, Nevada",
        "contact_type": ContactType.RADIO,
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli",
        "is_verified": False
    }

    print("Alien Contact Log Validation")
    print("======================================")
    validate(data)

    print("\n======================================")
    validate({**data, "contact_id": "BC_2024_001"})
    print("\n======================================")
    validate({**data, "contact_type": "physical"})
    print("\n======================================")
    validate({**data, "message_received": ""})
    print("\n======================================")
    validate({**data, "contact_type": "telepathic", "witness_count": 2})


if __name__ == "__main__":
    main()
