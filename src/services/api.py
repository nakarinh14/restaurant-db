from .db import Database

database = Database()

def get_restaurants_api():
    return database.retrive_rows("SELECT * FROM restaurants")

def get_restaurants_by_id_api(id: int):
    return database.retrive_single(f"SELECT * FROM restaurants r WHERE r.id={id}")

def get_restaurants_review_by_id_api(id: int):
    return database.retrive_rows(
        f"SELECT * FROM restaurants_reviews rr WHERE rr.restaurant_id={id}"
    )
