import hashlib

from . import api
from objects.user_account import UserAccount


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


def add_new_account(account: UserAccount) -> bool:
    user_id = add_new_user(account.username, account.password)
    if user_id:
        profile_id = api.add_new_user_profile_api(user_id, account.firstname, account.lastname, account.phone_number)
        if profile_id:
            print("Successfully register account {}".format(account.username))
            return True
        else:
            api.delete_user_api(user_id)
    print("Fail to register account {}".format(account.username))
    return False


def add_new_user(username: str, password: str):
    if api.get_user_by_username_api(username):
        print("User already exist")
        return None
    hash_password = hashlib.md5(password.encode()).hexdigest()
    return api.add_user_api(username, hash_password)
