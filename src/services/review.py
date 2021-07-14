from src.objects.review import Review

from . import api


def add_restaurant_review(review: Review) -> bool:
    rating_id = api.add_review_rating_api(review.rating)
    if rating_id is not None:
        review_id = api.add_review_api(review.user_profile_id, review.restaurant_id, review.rating, review.description,
                                       review.created_on)
        if review_id:
            print("Successfully Write a review")
            return True
        api.delete_review_rating(rating_id)
    print("Fail to write a review")
    return False
