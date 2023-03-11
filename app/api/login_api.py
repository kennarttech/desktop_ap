import requests
from flask_restful import Resource, Api
from flask import Flask, jsonify, request, render_template



app = Flask(__name__)


app.config['SECRETE_KEY'] = '81e8b01d5f87014ac298'
api = Api(app)


stores = [
    {
        "name": "My Wonderful Store",
        "items":[
            {
            "name": "My Item",
            "price": 15.99
            }
        ]
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


"""http://192.168.43.164:4000/store"""
@app.route('/store', methods=['POST']) 
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


"""GET store /store/<string:name>"""
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'that item is not in the store'})


"""GET store"""
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


"""POST /store<string:name>/item {name:, price}"""
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})
    

"""GET /store<string:name>/item"""
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'item not found'})




if __name__ == '__main__':
    app.run(port=5000, debug=True)