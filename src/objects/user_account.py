from dataclasses import dataclass

@dataclass
class UserAccount:
    username: str
    password: str
    firstname: str
    lastname: str
    phone_number: str
