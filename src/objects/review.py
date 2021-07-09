class Review:
    def __init__(self, user_profile_id, restaurant_id, rating, description, created_on):
        self.user_profile_id = user_profile_id
        self.restaurant_id = restaurant_id
        self.rating = rating
        self.description = description
        self.create_on = created_on
