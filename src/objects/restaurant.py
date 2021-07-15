from dataclasses import dataclass


@dataclass
class Restaurant:
    name: str
    phone_contact: str
    address: str
    create_on: str
    is_open: bool
