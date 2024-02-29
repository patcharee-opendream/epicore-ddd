from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from modules.rfi.value_objects import (
    Location,
    Organization,
    Recipient,
    Source,
    Syndrome,
)

# =============
# Python 3.11.5
# =============


class RfiStatus(Enum):
    OPENED = "OPENED"
    CLOSED = "CLOSED"
    REOPENED = "REOPENED"


class RfiOutcome(Enum):
    VERIFIED = "VERIFIED"
    UNVERIFIED = "UNVERIFIED"
    UPDATED = "UPDATED"


class RfiAffectedPopulation(Enum):
    HUMAN = "HUMAN"
    ANIMAL = "ANIMAL"
    ENVIRONMENTAL = "ENVIRONMENTAL"
    OTHER = "OTHER"


# =============
# model Requester
# =============
@dataclass
class Requester:
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    organization: Organization


# =============
# model RFI
# =============
@dataclass
class Rfi:
    id: int
    title: str
    date: datetime
    location: Location  # ตำแหน่งที่เกิดเหตุ
    responder_area: list[Location]  # พื้นที่ที่เกิดเหตุ
    requester: Requester  # ผู้แจ้งเหตุ
    recipients: list[Recipient]  # ผู้รับเรื่อง
    status: RfiStatus
    outcome: RfiOutcome
    affected_population: RfiAffectedPopulation
    affected_population_text: str
    health_condition_description: str
    sources: list[Source]  # แหล่งที่มาของข้อมูล
    syndromes: list[Syndrome]  # อาการ
