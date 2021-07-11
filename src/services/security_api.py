import hashlib

from src.objects.user_account import User_Account
from .db import Database

database = Database()


def authenticate(username: str, password: str) -> bool:
    if is_user_exist_by_username(username) and check_password_api(username, password):
        print("Successfully Login as {}".format(username))
        return True
    return False


def check_password_api(username: str, password: str) -> bool:
    input_hash_password = hashlib.md5(password.encode()).hexdigest()
    db_hash_password = get_password_by_username(username)
    return input_hash_password == db_hash_password


def get_user_by_id(user_id: int):
    return database.retrieve_single("SELECT * FROM users u WHERE u.user_id=%s", (user_id,))


def get_user_profile_by_user_id(user_id: int):
    return database.retrieve_single("SELECT * FROM user_profiles p WHERE p.user_id=%s", (user_id,))


def get_user_by_username(username: str):
    return database.retrieve_single("SELECT * FROM users u WHERE u.username=%s", (username,))


def is_user_exist_by_id(user_id: int) -> bool:
    row = get_user_by_id(user_id)
    return row is not None


def is_user_exist_by_username(username: str) -> bool:
    row = get_user_by_username(username)
    return row is not None


def is_user_profile_exist(user_id: int) -> bool:
    row = get_user_profile_by_user_id(user_id)
    return row is not None


def get_user_id_by_username(username: str) -> int:
    return database.retrieve_single("SELECT user_id FROM users u WHERE u.username=%s", (username,))[0]


def get_username_by_id(user_id) -> str:
    return database.retrieve_single("SELECT username FROM users u WHERE u.user_id=%s", (user_id,))[0]


def get_password_by_username(username: str) -> str:
    return database.retrieve_single("SELECT password FROM users u WHERE u.username=%s", (username,))[0]


def add_new_account_api(account: User_Account) -> bool:
    user_id = add_new_user_api(account.username, account.password)
    if user_id is not None:
        profile_id = add_new_user_profile_api(user_id, account.firstname, account.lastname, account.phone_number)
        if profile_id is not None:
            print("Successfully register account {}".format(account.username))
            return True
        else:
            delete_user_api(user_id)
    print("Fail to register account {}".format(account.username))
    return False


def add_new_user_api(username: str, password: str):
    if get_user_by_username(username) is not None:
        print("User already exist")
        return None
    hash_password = hashlib.md5(password.encode()).hexdigest()
    return database.insert_row(
        "INSERT INTO users(username, password) VALUES (%s, %s) RETURNING user_id", (username, hash_password,))


def add_new_user_profile_api(user_id: int, firstname: str, lastname: str, phone_number: str):
    return database.insert_row(
        "INSERT INTO user_profiles(user_id, firstname ,lastname, phone_contact) VALUES (%s, %s, %s, %s) RETURNING "
        "user_profile_id",
        (user_id, firstname, lastname, phone_number,))


def delete_user_api(user_id):
    return database.delete_row("DELETE FROM users u WHERE u.user_id=%s", (user_id,))


def delete_account_api(user_id):
    database.delete_row("DELETE FROM user_profiles p WHERE p.user_id=%s", (user_id,))
    database.delete_row("DELETE FROM users u WHERE u.user_id=%s", (user_id,))
    if is_user_exist_by_id(user_id) or is_user_profile_exist(user_id):
        print("Fail to delete an account")
    else:
        print("Successfully delete an account")
    return
