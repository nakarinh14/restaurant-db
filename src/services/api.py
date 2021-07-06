from .db import Database

database = Database()

# Don't use string interpolating or concatenation!

def get_all_restaurants_api():
    return database.retrive_rows("SELECT * FROM restaurants")

def get_restaurants_by_id_api(id: int):
    return database.retrive_single("SELECT * FROM restaurants r WHERE r.id=%s", (id,))

def get_restaurants_review_by_id_api(id: int):
    return database.retrive_rows(
        "SELECT * FROM restaurants_reviews rr WHERE rr.restaurant_id=%s", (id,)
    )
