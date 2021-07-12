import hashlib

from src.objects.review import Review
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


def add_new_account(account: UserAccount) -> bool:
    user_id = add_new_user(account.username, account.password)
    profile_id = api.add_new_user_profile_api(user_id, account.firstname, account.lastname, account.phone_number)
    if user_id is not None and profile_id is not None:
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


def add_restaurant_review(review: Review) -> bool:
    rating_id = api.add_review_rating_api(review.rating)
    if rating_id is not None:
        review_id = api.add_review_api(review.user_profile_id, review.restaurant_id,
                                       review.rating, review.description, review.created_on)
        if review_id is not None:
            print("Successfully Write a review")
            return True
        api.delete_review_rating(rating_id)
    print("Fail to write a review")
    return False

