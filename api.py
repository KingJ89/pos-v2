# api.py
from flask import Flask, jsonify, request
from backend import *

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    inventory = get_inventory()
    return jsonify({'products': inventory})

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    price = data.get('price')
    quantity = data.get('quantity')
    add_product_to_inventory(name, price, quantity)
    return jsonify({'message': 'Product added successfully.'})

@app.route('/products/<int:product_id>', methods=['PUT'])
def sell_product(product_id):
    data = request.get_json()
    quantity = data.get('quantity')
    if sell_product(product_id, quantity):
        return jsonify({'message': 'Product sold successfully.'})
    else:
        return jsonify({'message': 'Insufficient quantity.'}), 400

if __name__ == "__main__":
    app.run(debug=True)

