from dataclasses import dataclass


@dataclass(frozen=True)
class Organization:
    name: str


@dataclass(frozen=True)
class Location:
    name: str
    lat: float
    lon: float


@dataclass(frozen=True)
class Recipient:
    first_name: str
    last_name: str
    email: str
    phone: str
    organization: Organization


@dataclass(frozen=True)
class Source:
    name: str
    url: str


@dataclass(frozen=True)
class Syndrome:
    name: str
