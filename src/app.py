from flask import Flask
from flask import request

from services import api, auth
from services.utils import wrap_json_data

app = Flask(__name__)


@app.route('/api/restaurants', methods=['GET'])
def restaurants():
    restaurant_id = request.args.get('id')
    if not restaurant_id:
        data = api.get_all_restaurants_api()
        return wrap_json_data(data)
    else:
        data = api.get_restaurants_by_id_api(restaurant_id)
        return wrap_json_data(data)


@app.route('/api/restaurants/reviews', methods=['GET'])
def restaurants_reviews():
    restaurant_id = request.args.get('id')
    if restaurant_id:
        data = api.get_restaurants_review_by_id_api(restaurant_id)
        return wrap_json_data(data)


@app.route('/api/restaurants/menus', methods=['GET'])
def restaurants_menus():
    restaurant_id = request.args.get('id')
    if restaurant_id:
        data = api.get_all_menu_by_restaurant_id_api(restaurant_id)
        return wrap_json_data(data)


@app.route('/auth', methods=['POST'])
def auth_view():
    credentials = request.json
    if credentials:
        status = auth.authenticate(credentials.get('username'), credentials.get('password'))
        return {'status': status}
