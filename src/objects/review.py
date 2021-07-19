from dataclasses import dataclass


@dataclass
class Review:
    user_profile_id: str
    restaurant_id: str
    rating: str
    description: str
