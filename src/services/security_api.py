import hashlib

from src.objects.user_profile import User_Profile
from .db import Database

database = Database()


def get_user_by_username(username: str):
    return database.retrieve_single("SELECT * FROM users u WHERE u.username=%s", (username,))


def is_user_exist(username: str) -> bool:
    row = get_user_by_username(username)
    return row is not None


def get_username_by_id(user_id) -> str:
    return database.retrieve_single("SELECT username FROM users u WHERE u.user_id=%s", (user_id,))[0]


def get_password_by_username(username: str) -> str:
    return database.retrieve_single("SELECT password FROM users u WHERE u.username=%s", (username,))[0]


def add_new_account_api(profile: User_Profile) -> bool:
    user_id = add_new_user_api(profile.username, profile.password)
    if user_id is not None:
        profile_id = add_new_user_profile_api(user_id, profile.firstname, profile.lastname, profile.phone_number)
        if profile_id is not None:
            print("Successfully register account {}".format(profile.username))
            return True
        else:
            delete_user_api(user_id)
    print("Fail to register account {}".format(profile.username))
    return False


def check_password_api(username: str, password: str) -> bool:
    input_hash_password = hashlib.md5(password.encode()).hexdigest()
    db_hash_password = get_password_by_username(username)
    return input_hash_password == db_hash_password


def add_new_user_api(username: str, password: str):
    if get_user_by_username(username) is not None:
        print("User already exist")
        return None
    hash_password = hashlib.md5(password.encode()).hexdigest()
    return database.insert_row(
        "INSERT INTO users(username, password) VALUES (%s, %s) RETURNING user_id", (username, hash_password,))


def add_new_user_profile_api(user_id: int, firstname: str, lastname: str, phone_number: str):
    return database.insert_row(
        "INSERT INTO user_profiles(user_id, firstname ,lastname, phone_contact) VALUES (%d, %s, %s, %s) RETURNING "
        "user_profile_id",
        (user_id, firstname, lastname, phone_number,))


def delete_user_api(user_id):
    return database.delete_row("DELETE FROM users u WHERE u.user_id=%s", (user_id,))


def delete_account_api(user_id):
    database.delete_row("DELETE FROM user_profiles p WHERE p.user_id=%s", (user_id,))
    database.delete_row("DELETE FROM users u WHERE u.user_id=%s", (user_id,))
    # TODO: add feature to check if successfully delete or not
    return
