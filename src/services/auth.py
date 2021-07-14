import hashlib

from src.objects.user_account import UserAccount
from . import api


def authenticate(username: str, password: str) -> bool:
    if not username or not password:
        return False
    db_user = api.get_user_by_username_api(username)
    if db_user and compare_password(password, db_user.get('password')):
        print("Successfully Login as {}".format(username))
        return True
    return False


def compare_password(input_password, db_hash_password):
    input_hash_password = hashlib.md5(input_password.encode()).hexdigest()
    return input_hash_password == db_hash_password


def is_user_exist_by_id(user_id: int) -> bool:
    return bool(api.get_user_by_id_api(user_id))


def is_user_exist_by_username(username: str) -> bool:
    return bool(api.get_user_by_username_api(username))


def is_user_profile_exist(user_id: int) -> bool:
    return bool(api.get_user_profile_by_user_id_api(user_id))


def register(account: UserAccount) -> bool:
    user_id = add_new_user(account.username, account.password)
    profile_id = api.add_new_user_profile_api(user_id, account.firstname, account.lastname, account.phone_number)
    if user_id and profile_id:
        print("Successfully register account {}".format(account.username))
        return True
    api.delete_account_api(user_id)
    print("Fail to register account {}".format(account.username))
    return False


def add_new_user(username: str, password: str):
    if api.get_user_by_username_api(username):
        print("User already exist")
        return None
    hash_password = hashlib.md5(password.encode()).hexdigest()
    return api.add_user_api(username, hash_password)


def delete_account(user_id: int) -> bool:
    username = api.get_username_by_id_api(user_id)
    api.delete_account_api(user_id)
    if not is_user_exist_by_id(user_id) and not is_user_profile_exist(user_id):
        print("Successfully Delete Account {}".format(username))
        return True
    print("Fail to Delete Account {}".format(username))
    return False
