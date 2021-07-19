from objects.restaurant import Restaurant

from .db import Database

database = Database()


# Restaurants

def get_all_restaurants_api():
    return database.retrieve_rows("SELECT * FROM restaurant")


def get_restaurants_by_id_api(restaurant_id):
    return database.retrieve_single("SELECT * FROM restaurant r WHERE r.restaurant_id=%s", (restaurant_id,))


def get_restaurants_review_by_id_api(restaurant_id):
    return database.retrieve_rows(
        "SELECT * FROM review rr WHERE rr.restaurant_id=%s", (restaurant_id,)
    )


def get_all_menu_by_restaurant_id_api(restaurant_id):
    return database.retrieve_rows("SELECT * FROM menu WHERE restaurant_id=%s", (restaurant_id,))


def get_menu_by_id_api(menu_id):
    return database.retrieve_single("SELECT * FROM menu WHERE menu_id=%s", (menu_id,))


def add_new_restaurant_api(restaurant: Restaurant):
    return database.insert_row(
        "INSERT INTO restaurant(name, phone_contact, address, user_owner_id) "
        "VALUES (%s, %s, %s, %s) RETURNING restaurant_id",
        (restaurant.name, restaurant.phone_contact, restaurant.address, restaurant.user_owner_id))


# Reviews


def add_review_rating_api(score):
    return database.insert_row("INSERT INTO rating(score) VALUES (%s) RETURNING rating_id", (score,))


def add_review_api(user_profile_id, restaurant_id, rating_id, description):
    return database.insert_row(
        "INSERT INTO review(user_profile_id, restaurant_id, rating_id, description) "
        "VALUES (%s, %s, %s, %s) RETURNING review_id",
        (user_profile_id, restaurant_id, rating_id, description))


def delete_review_rating(rating_id):
    return database.delete_row("DELETE FROM rating WHERE rating_id=%s", (rating_id,))


# Users


def get_user_by_id_api(user_id):
    return database.retrieve_single("SELECT * FROM user u WHERE u.user_id=%s", (user_id,))


def get_user_profile_by_user_id_api(user_id):
    return database.retrieve_single("SELECT * FROM user_profile p WHERE p.user_id=%s", (user_id,))


def get_user_by_username_api(username):
    return database.retrieve_single("SELECT * FROM user u WHERE u.username=%s", (username,))


def get_username_by_id_api(user_id) -> str:
    return database.retrieve_single("SELECT username FROM user u WHERE u.user_id=%s", (user_id,)).get('username')


def get_password_by_username_api(username: str) -> str:
    return database.retrieve_single("SELECT password FROM user u WHERE u.username=%s", (username,)).get('password')


def get_user_id_by_username_api(username: str) -> int:
    return database.retrieve_single("SELECT user_id FROM user u WHERE u.username=%s", (username,)).get('user_id')


def add_user_api(username: str, hash_password: str):
    return database.insert_row(
        "INSERT INTO user(username, password) VALUES (%s, %s) RETURNING user_id", (username, hash_password,))


def add_new_user_profile_api(user_id, firstname, lastname, phone_number):
    return database.insert_row(
        "INSERT INTO user_profile(user_id, firstname ,lastname, phone_contact) VALUES (%s, %s, %s, %s) RETURNING "
        "user_profile_id",
        (user_id, firstname, lastname, phone_number,))


def delete_account_api(user_id):
    return database.delete_row("DELETE FROM user u WHERE u.user_id=%s", (user_id,))


# Tagging


def add_tag_to_restaurant(restaurant_id, tag_id):
    return database.insert_row("INSERT INTO restaurant_tag(tag_id, restaurant_id) "
                               "VALUES (%s,%s) RETURNING restaurant_tag_id", (tag_id, restaurant_id,))


# menu

def add_new_menu_to_restaurant(restaurant_id, menu_type_id, name, list_pricing):
    return database.insert_row("INSERT INTO menu(restaurant_id, menu_type_id, name, list_pricing) "
                               "VALUES (%s,%s,%s,%s) RETURNING menu_id",
                               (restaurant_id, menu_type_id, name, list_pricing))


def is_menu_exist_in_restaurant(menu_name: str, restaurant_id):
    return bool(database.retrieve_single("SELECT * FROM menu WHERE name=%s AND restaurant_id=%s",
                                         (menu_name, restaurant_id)))
