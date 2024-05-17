# backend.py
import json
import sqlite3
from datetime import datetime

# JSON file path
JSON_FILE = 'data/inventory.json'
# SQLite database path
DB_FILE = 'inventory.db'

def setup_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def load_inventory_from_json():
    try:
        with open(JSON_FILE, 'r') as f:
            inventory = json.load(f)
    except FileNotFoundError:
        inventory = []
    return inventory

def save_inventory_to_json(inventory):
    with open(JSON_FILE, 'w') as f:
        json.dump(inventory, f, indent=4)

def add_product_to_db(name, price, quantity):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)
    ''', (name, price, quantity))
    conn.commit()
    conn.close()

def add_product_to_inventory(name, price, quantity):
    inventory = load_inventory_from_json()
    product = {
        'id': len(inventory) + 1,
        'name': name,
        'price': price,
        'quantity': quantity
    }
    inventory.append(product)
    save_inventory_to_json(inventory)
    add_product_to_db(name, price, quantity)

def sell_product(product_id, quantity):
    inventory = load_inventory_from_json()
    for product in inventory:
        if product['id'] == product_id:
            if product['quantity'] >= quantity:
                product['quantity'] -= quantity
                save_inventory_to_json(inventory)
                return True
            else:
                return False
    return False

def get_inventory():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    inventory = cursor.fetchall()
    conn.close()
    return inventory

def generate_report():
    inventory = load_inventory_from_json()
    total_value = sum(product['price'] * product['quantity'] for product in inventory)
    report = {
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'total_value': total_value,
        'inventory': inventory
    }
    return report

