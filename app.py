from flask import Flask, request, jsonify
from flask_cors import CORS

# ===== YOUR EXISTING CLASSES =====
class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Snacks:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def total(self):
        return sum(item["price"] for item in self.items)

    def clear(self):
        self.items.clear()

# ===== FLASK SETUP =====
app = Flask(__name__)
CORS(app)

order = Order()

coffee_menu = [
    Coffee("Espresso", 2.5),
    Coffee("Latte", 3.5),
    Coffee("Cappuccino", 3.0),
    Coffee("Americano", 2.0),
    Coffee("Doppio", 2.5),
    Coffee("Mocha", 2.65),
    Coffee("Affogato", 2.8),
    Coffee("Frappe", 3.0),
    Coffee("Macchiato", 3.25),
    Coffee("Filter Coffee", 1.5)
]

snacks_menu = [
    Snacks("Muffin", 3.0),
    Snacks("Croissant", 2.0),
    Snacks("Cookie", 1.5),
    Snacks("Nacho", 2.5),
    Snacks("Cinnamon Roll", 1.5),
    Snacks("Donut", 3.0),
    Snacks("Cheesecake", 3.5),
    Snacks("Brownies", 3.0),
    Snacks("Blondies", 2.75),
    Snacks("Toast", 2.0)
]

# ===== API ROUTES =====
@app.route("/menu", methods=["GET"])
def get_menu():
    return jsonify({
        "coffee": [
            {"name": "Espresso", "price": 2.5, "image": "espresso.jpg"},
            {"name": "Latte", "price": 3.5, "image": "latte.jpg"},
            {"name": "Cappuccino", "price": 3.0, "image": "Capuccino.jpg"},
            {"name": "Americano", "price": 2.0, "image": "americano.jpg"},
            {"name": "Doppio", "price": 2.5, "image": "dopio.jpg"},
            {"name": "Mocha", "price": 2.65, "image": "mocha.jpg"},
            {"name": "Affogato", "price": 2.8, "image": "affogato.jpg"},
            {"name": "Frappe", "price": 3.0, "image": "frappe.jpg"},
            {"name": "Macchiato", "price": 3.25, "image": "macchiato.jpg"},
            {"name": "Filter Coffee", "price": 1.5, "image": "filter.jpg"}
        ],
        "snacks": [
            {"name": "Muffin", "price": 3.0, "image": "muffin.jpg"},
            {"name": "Croissant", "price": 2.0, "image": "croissant.jpg"},
            {"name": "Cookie", "price": 1.5, "image": "cookies.jpg"},
            {"name": "Donut", "price": 3.0, "image": "donut.jpg"},
            {"name": "Nacho", "price": 2.5, "image": "nacho.jpg"},
            {"name": "Cinnamon Roll", "price": 1.5, "image": "cinnamonroll.jpg"},
            {"name": "Cheesecake", "price": 3.5, "image": "cheesecake.jpg"},
            {"name": "Brownies", "price": 3.0, "image": "brownies.jpg"},
            {"name": "Blondies", "price": 2.75, "image": "blondies.jpg"},
            {"name": "Toast", "price": 2.0, "image": "toast.jpg"}
        ]
    })


@app.route("/add-item", methods=["POST"])
def add_item():
    data = request.json
    print("Received item:", data)   # 👈 DEBUG
    order.add_item(data)
    return jsonify({"message": "Item added", "order": order.items})


@app.route("/order", methods=["GET"])
def view_order():
    print("Order requested")        # 👈 DEBUG
    return jsonify({
        "items": order.items,
        "total": order.total()
    })


@app.route("/checkout", methods=["POST"])
def checkout():
    total = order.total()
    order.clear()
    return jsonify({"message": "Order confirmed", "total": total})

# ===== RUN SERVER =====
if __name__ == "__main__":
    app.run(debug=True)
