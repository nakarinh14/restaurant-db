from .db import Database

database = Database()


# Don't use string interpolating or concatenation!

def get_all_restaurants_api():
    return database.retrieve_rows("SELECT * FROM restaurants")


def get_restaurants_by_id_api(restaurant_id):
    return database.retrieve_single("SELECT * FROM restaurants r WHERE r.restaurant_id=%s", (restaurant_id,))


def get_restaurants_review_by_id_api(restaurant_id):
    return database.retrieve_rows(
        "SELECT * FROM reviews rr WHERE rr.restaurant_id=%s", (restaurant_id,)
    )


def get_all_menu_by_restaurant_id_api(restaurant_id):
    return database.retrieve_rows("SELECT * FROM menus WHERE restaurant_id=%s", (restaurant_id,))


def get_menu_by_id_api(menu_id):
    return database.retrieve_single("SELECT * FROM menus WHERE menu_id=%s", (menu_id,))


def add_review_rating_api(score):
    return database.insert_row("INSERT INTO ratings(score) VALUES (%s) RETURNING rating_id", (score,))


def add_review_api(user_profile_id, restaurant_id, rating_id, description, created_on):
    return database.insert_row(
        "INSERT INTO reviews(user_profile_id, restaurant_id, rating_id, description, created_on) VALUES "
        "(%s, %s, %s, %s, %s::timestamp) RETURNING review_id",
        (user_profile_id, restaurant_id, rating_id, description, created_on))


def delete_review_rating(rating_id):
    return database.delete_row("DELETE FROM ratings WHERE rating_id=%s", (rating_id,))


def get_user_by_id_api(user_id):
    return database.retrieve_single("SELECT * FROM users u WHERE u.user_id=%s", (user_id,))


def get_user_profile_by_user_id_api(user_id):
    return database.retrieve_single("SELECT * FROM user_profiles p WHERE p.user_id=%s", (user_id,))


def get_user_by_username_api(username):
    return database.retrieve_single("SELECT * FROM users u WHERE u.username=%s", (username,))


def get_username_by_id_api(user_id) -> str:
    return database.retrieve_single("SELECT username FROM users u WHERE u.user_id=%s", (user_id,)).get('username')


def get_password_by_username_api(username: str) -> str:
    return database.retrieve_single("SELECT password FROM users u WHERE u.username=%s", (username,)).get('password')


def get_user_id_by_username_api(username: str) -> int:
    return database.retrieve_single("SELECT user_id FROM users u WHERE u.username=%s", (username,)).get('user_id')


def add_user_api(username: str, hash_password: str):
    return database.insert_row(
        "INSERT INTO users(username, password) VALUES (%s, %s) RETURNING user_id", (username, hash_password,))


def add_new_user_profile_api(user_id, firstname, lastname, phone_number):
    return database.insert_row(
        "INSERT INTO user_profiles(user_id, firstname ,lastname, phone_contact) VALUES (%s, %s, %s, %s) RETURNING "
        "user_profile_id",
        (user_id, firstname, lastname, phone_number,))


def delete_account_api(user_id):
    return database.delete_row("DELETE FROM users u WHERE u.user_id=%s", (user_id,))
