from modules.rfi.aggregate.model import (
    Requester,
    Rfi,
    RfiAffectedPopulation,
    RfiOutcome,
    RfiStatus,
)
from modules.rfi.value_objects import (
    Location,
    Organization,
    Recipient,
    Source,
    Syndrome,
)
import pytest
from datetime import datetime


@pytest.fixture
def requester():
    return Requester.new_requester(
        first_name="John",
        last_name="Doe",
        email="test@gmail.com",
        phone="1234567890",
        organization=Organization(name="opendream"),
    )


@pytest.fixture
def rfi():
    location = Location(name="Bangkok", lat=13.7563, lon=100.5018)
    responder_area = [Location(name="Korea", lat=35.9078, lon=127.7669), location]

    recipient = Recipient(
        first_name="Jane",
        last_name="Doe",
        email="jane@gmail.com",
        phone="0987654321",
        organization=Organization(name="epicore"),
    )
    sources = [
        Source(name="WHO", url="https://www.who.int/"),
        Source(name="CDC", url="https://www.cdc.gov/"),
    ]
    syndromes = [Syndrome(name="COVID-19"), Syndrome(name="MERS")]
    today = datetime.now()

    # Create a new RFI
    rfi = Rfi.new_rfi(
        title="COVID-19 Outbreak in Bangkok",
        date=today,
        location=location,
        responder_area=responder_area,
        requester=requester,
        recipients=[recipient],
        outcome=RfiOutcome.UPDATED,
        affected_population=RfiAffectedPopulation.HUMAN,
        affected_population_text="",
        health_condition_description="",
        sources=sources,
        syndromes=syndromes,
    )
    return rfi


def test_create_rfi(requester):
    location = Location(name="Bangkok", lat=13.7563, lon=100.5018)
    responder_area = [Location(name="Korea", lat=35.9078, lon=127.7669), location]

    recipient_1 = Recipient(
        first_name="Jane",
        last_name="Doe",
        email="jane@gmail.com",
        phone="0987654321",
        organization=Organization(name="epicore"),
    )
    recipient_2 = Recipient(
        first_name="John",
        last_name="Doe",
        email="john@gmail.com",
        phone="1234567890",
        organization=Organization(name="โรงพยาบาลกรุงเทพ"),
    )

    sources = [
        Source(name="WHO", url="https://www.who.int/"),
        Source(name="CDC", url="https://www.cdc.gov/"),
    ]
    syndromes = [Syndrome(name="COVID-19"), Syndrome(name="MERS")]
    today = datetime.now()

    # Create a new RFI
    rfi = Rfi.new_rfi(
        title="COVID-19 Outbreak in Bangkok",
        date=today,
        location=location,
        responder_area=responder_area,
        requester=requester,
        recipients=[recipient_1, recipient_2],
        outcome=RfiOutcome.UPDATED,
        affected_population=RfiAffectedPopulation.HUMAN,
        affected_population_text="",
        health_condition_description="",
        sources=sources,
        syndromes=syndromes,
    )

    assert rfi.title == "COVID-19 Outbreak in Bangkok"
    assert rfi.date == today
    assert rfi.location == location
    assert rfi.responder_area == responder_area
    assert rfi.requester == requester
    assert rfi.recipients == [recipient_1, recipient_2]
    assert rfi.outcome == RfiOutcome.UPDATED
    assert rfi.affected_population == RfiAffectedPopulation.HUMAN
    assert rfi.affected_population_text == ""
    assert rfi.health_condition_description == ""
    assert rfi.sources == sources
    assert rfi.syndromes == syndromes
    assert rfi.status == RfiStatus.OPENED


def test_close_rfi(rfi):
    assert rfi.status == RfiStatus.OPENED
    rfi.close()
    assert rfi.status == RfiStatus.CLOSED


def test_reopen_rfi(rfi):
    rfi.close()
    assert rfi.status == RfiStatus.CLOSED
    rfi.reopen()
    assert rfi.status == RfiStatus.REOPENED
