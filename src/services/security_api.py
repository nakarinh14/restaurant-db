import hashlib

from src.objects.user_profile import User_Profile
from .db import Database

database = Database()


def get_user_by_username(username: str):
    return database.retrieve_single("SELECT * FROM users u WHERE u.username=%s", (username,))


def get_username_by_id(user_id):
    return database.retrieve_single("SELECT username FROM users u WHERE u.user_id=%s", (user_id,))


def add_new_account_api(profile: User_Profile):
    user_id = add_new_user_api(profile.username, profile.password)
    if ((user_id is not None) and
            (add_new_user_profile_api(user_id, profile.firstname, profile.lastname, profile.phone_number) is not None)):
        print("Successfully register account {}".format(profile.username))
        return True
    print("Fail to register account {}".format(profile.username))
    return False


def add_new_user_api(username: str, password: str):
    if get_user_by_username(username) is not None:
        print("User already exist")
        return None
    hash_password = hashlib.md5(password.encode())
    return database.insert_row(
        "INSERT INTO users(username, password) VALUES (%s, %s)", (username, hash_password,))


def add_new_user_profile_api(user_id: int, firstname: str, lastname: str, phone_number: str):
    return database.insert_row(
        "INSERT INTO user_profiles(user_id, firstname ,lastname, phone_contact) VALUES (%d, %s, %s, %s)",
        (user_id, firstname, lastname, phone_number,))
