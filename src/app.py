from flask import Flask
from flask import request

from services import api

app = Flask(__name__)

@app.route('/restaurants', methods=['GET'])
def restaurants():
    restaurant_id = request.args.get('id')
    if not restaurant_id:
        return api.get_all_restaurants_api()
    else:
        return api.get_restaurants_by_id_api(restaurant_id)

@app.route('/restaurants/reviews', methods=['GET'])
def restaurants_reviews():
    restaurant_id = request.args.get('id')
    if restaurant_id:
        return api.get_restaurants_review_by_id_api(restaurant_id)
    
