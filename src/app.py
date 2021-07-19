from flask import Flask
from flask import request

from objects.restaurant import Restaurant
from objects.review import Review
from objects.user_account import UserAccount
from services import api, auth, review
from services.utils import wrap_json_data

app = Flask(__name__)


# Restaurants

@app.route('/api/restaurants', methods=['GET'])
def restaurants():
    restaurant_id = request.args.get('id')
    if not restaurant_id:
        data = api.get_all_restaurants_api()
        return wrap_json_data(data)
    else:
        data = api.get_restaurants_by_id_api(restaurant_id)
        return wrap_json_data(data)


@app.route('/api/restaurants', methods=['POST'])
def restaurants_post():
    data = request.json
    keys = ("name", "phone_contact", "address", "user_owner_id")
    if data and all([k in data for k in keys]):
        new_restaurant = Restaurant(**data)
        status = bool(api.add_new_restaurant_api(new_restaurant))
        return {'status': status}
    return {'status': False}


@app.route('/api/restaurants/reviews', methods=['GET'])
def restaurants_reviews():
    restaurant_id = request.args.get('id')
    if restaurant_id:
        data = api.get_restaurants_review_by_id_api(restaurant_id)
        return wrap_json_data(data)


@app.route('/api/restaurants/reviews', methods=['POST'])
def restaurants_reviews_post():
    data = request.json
    keys = ("user_profile_id", "restaurant_id", "rating", "description")
    if data and all([k in data for k in keys]):
        # Apply review for given restaurant id.
        new_review = Review(**data)
        status = bool(review.add_restaurant_review(new_review))
        return {'status': status}
    return {'status': False}


@app.route('/api/restaurants/menus', methods=['GET'])
def restaurants_menus():
    restaurant_id = request.args.get('id')
    if restaurant_id:
        data = api.get_all_menu_by_restaurant_id_api(restaurant_id)
        return wrap_json_data(data)


@app.route('/api/restaurants/menus', methods=['POST'])
def restaurants_menus_post():
    data = request.json
    restaurant_id = data.get('restaurant_id')
    menu_type = data.get('menu_type_id')
    name = data.get('name')
    list_pricing = data.get('list_pricing')
    if not api.is_menu_exist_in_restaurant(name, restaurant_id):
        status = bool(api.add_new_menu_to_restaurant(restaurant_id, menu_type, name, list_pricing))
        return {'status': status}
    return {'status': False}


@app.route('/register', methods=['POST'])
def register_view():
    data = request.json
    keys = ('username', 'password', 'firstname', 'lastname', 'phone_number')
    if data and all([k in data for k in keys]):
        account_obj = UserAccount(**data)
        status = auth.register(account_obj)
        return {'status': status}
    return {'status': False}


@app.route('/auth', methods=['POST'])
def auth_view():
    credentials = request.json
    if credentials:
        status = auth.authenticate(credentials.get('username'), credentials.get('password'))
        return {'status': status}
