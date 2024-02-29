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

    @staticmethod
    def new_requester(
        first_name: str,
        last_name: str,
        email: str,
        phone: str,
        organization: Organization,
    ) -> "Requester":
        return Requester(
            id=0,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            organization=organization,
        )


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

    @staticmethod
    def new_rfi(
        title: str,
        date: datetime,
        location: Location,
        responder_area: list[Location],
        requester: Requester,
        recipients: list[Recipient],
        outcome: RfiOutcome,
        affected_population: RfiAffectedPopulation,
        affected_population_text: str,
        health_condition_description: str,
        sources: list[Source],
        syndromes: list[Syndrome],
    ) -> "Rfi":
        return Rfi(
            id=0,
            title=title,
            date=date,
            location=location,
            responder_area=responder_area,
            requester=requester,
            recipients=recipients,
            status=RfiStatus.OPENED,
            outcome=outcome,
            affected_population=affected_population,
            affected_population_text=affected_population_text,
            health_condition_description=health_condition_description,
            sources=sources,
            syndromes=syndromes,
        )

    def close(self) -> None:
        self.status = RfiStatus.CLOSED

    def reopen(self) -> None:
        self.status = RfiStatus.REOPENED
