from .db import Database

database = Database()


# Don't use string interpolating or concatenation!

def get_all_restaurants_api():
    return database.retrieve_rows("SELECT * FROM restaurants")


def get_restaurants_by_id_api(restaurant_id: int):
    return database.retrieve_single("SELECT * FROM restaurants r WHERE r.restaurant_id=%s", (restaurant_id,))


def get_restaurants_review_by_id_api(restaurant_id: int):
    return database.retrieve_rows(
        "SELECT * FROM reviews rr WHERE rr.restaurant_id=%s", (restaurant_id,)
    )


def get_all_menu_by_restaurant_id_api(restaurant_id: int):
    return database.retrieve_rows("SELECT * FROM menus WHERE restaurant_id=%s", (restaurant_id,))


def get_menu_by_id_api(menu_id: int):
    return database.retrieve_single("SELECT * FROM menus WHERE menu_id=%s", (menu_id,))
