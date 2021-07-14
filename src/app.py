from flask import Flask
from flask import request

from services import api, auth
from services.utils import wrap_json_data
from objects.user_account import UserAccount

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
    # TODO: Add new restaurant
    data = request.json


@app.route('/api/restaurants/reviews', methods=['GET'])
def restaurants_reviews():
    restaurant_id = request.args.get('id')
    if restaurant_id:
        data = api.get_restaurants_review_by_id_api(restaurant_id)
        return wrap_json_data(data)


@app.route('/api/restaurants/reviews', methods=['POST'])
def restaurants_reviews_post():
    # TODO: Add review if exist yet in db, else update
    data = request.json
    if data:
        # Apply review for given restaurant id.
        pass


@app.route('/api/restaurants/menus', methods=['GET'])
def restaurants_menus():
    restaurant_id = request.args.get('id')
    if restaurant_id:
        data = api.get_all_menu_by_restaurant_id_api(restaurant_id)
        return wrap_json_data(data)


@app.route('/api/restaurants/menus', methods=['POST'])
def restaurants_menus_post():
    # TODO: Add menu if not exist yet in db, else update
    data = request.json
    if data:
        pass


@app.route('/register', methods=['POST'])
def register_view():
    data = request.json
    keys = ('username', 'password', 'firstname', 'lastname', 'phone_number')
    if data and all([k in data for k in keys]):
        account_obj = UserAccount(**data)
        status = auth.register(account_obj)
        return {'status': status}


@app.route('/auth', methods=['POST'])
def auth_view():
    credentials = request.json
    if credentials:
        status = auth.authenticate(credentials.get('username'), credentials.get('password'))
        return {'status': status}
