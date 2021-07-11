import hashlib

from . import api
from objects.user_account import UserAccount
from objects.review import Review


def authenticate(username: str, password: str) -> bool:
    if is_user_exist_by_username(username) and check_password_api(username, password):
        print("Successfully Login as {}".format(username))
        return True
    return False


def check_password_api(username: str, password: str) -> bool:
    input_hash_password = hashlib.md5(password.encode()).hexdigest()
    db_hash_password = api.get_password_by_username_api(username)
    return input_hash_password == db_hash_password


def is_user_exist_by_id(user_id: int) -> bool:
    return api.get_user_by_id_api(user_id) is not None


def is_user_exist_by_username(username: str) -> bool:
    return api.get_user_by_username_api(username) is not None


def is_user_profile_exist(user_id: int) -> bool:
    return api.get_user_profile_by_user_id_api(user_id) is not None


def add_new_account(account: UserAccount) -> bool:
    user_id = add_new_user(account.username, account.password)
    if user_id is not None:
        profile_id = api.add_new_user_profile_api(user_id, account.firstname, account.lastname, account.phone_number)
        if profile_id is not None:
            print("Successfully register account {}".format(account.username))
            return True
        else:
            api.delete_user_api(user_id)
    print("Fail to register account {}".format(account.username))
    return False


def add_new_user(username: str, password: str):
    if api.get_user_by_username_api(username) is not None:
        print("User already exist")
        return None
    hash_password = hashlib.md5(password.encode()).hexdigest()
    return api.add_user_api(username, hash_password)


def add_restaurant_review(review: Review) -> bool:
    rating_id = api.add_review_rating_api(review.rating)
    if rating_id is not None:
        review_id = api.add_review_api(review.user_profile_id, review.restaurant_id, review.rating, review.description, review.created_on)
        if review_id is not None:
            print("Successfully Write a review")
            return True
        api.delete_review_rating(rating_id)
    print("Fail to write a review")
    return False
