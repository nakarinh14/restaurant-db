from src.objects.review import Review
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


def add_review_rating(score: int):
    return database.insert_row("INSERT INTO ratings(score) VALUES (%s) RETURNING rating_id", (score,))


def delete_review_rating(rating_id: int):
    return database.delete_row("DELETE FROM ratings WHERE rating_id=%s", (rating_id,))


def add_restaurant_review(review: Review) -> bool:
    rating_id = add_review_rating(review.rating)
    if rating_id is not None:
        review_id = database.insert_row(
            "INSERT INTO reviews(user_profile_id, restaurant_id, rating_id, description, created_on) VALUES "
            "(%s, %s, %s, %s, %s::timestamp) RETURNING review_id",
            (review.user_profile_id, review.restaurant_id, rating_id, review.description, review.create_on))
        if review_id is not None:
            print("Successfully Write a review")
            return True
        else:
            delete_review_rating(rating_id)
    print("Fail to write a review")
    return False
