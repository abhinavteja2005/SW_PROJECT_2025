# Stores data with inventory and location coordinates
from uuid import uuid4

stores = {
    1: {
        "name": "Store A",
        "location": (0, 0),
        "manager": "manager1",
        "items": {
            "Apple": {"price": 10, "stock": 20, "discount": 0, "item_type": "Fruits"},
            "3 Apples": {"price": 30, "stock": 5, "discount": 10, "item_type": "Fruits"},
            "Banana": {"price": 5, "stock": 30, "discount": 10, "item_type": "Fruits"},
            "Milk": {"price": 50, "stock": 15, "discount": 0, "item_type": "Dairy"},
            "Bread": {"price": 25, "stock": 10, "discount": 5, "item_type": "Bakery"},
            "Eggs": {"price": 60, "stock": 24, "discount": 0, "item_type": "Dairy"},
            "Rice": {"price": 70, "stock": 25, "discount": 5, "item_type": "Grains"},
            "Pasta": {"price": 35, "stock": 18, "discount": 0, "item_type": "Grains"},
            "Tomatoes": {"price": 15, "stock": 22, "discount": 0, "item_type": "Vegetables"},
            "Potatoes": {"price": 20, "stock": 30, "discount": 5, "item_type": "Vegetables"},
            "Chicken": {"price": 120, "stock": 10, "discount": 0, "item_type": "Meat"},
        }
    },
    2: {
        "name": "Store B",
        "location": (2, 3),
        "manager": "manager2",
        "items": {
            "Apple": {"price": 12, "stock": 15, "discount": 5, "item_type": "Fruits"},
            "Banana": {"price": 7, "stock": 20, "discount": 0, "item_type": "Fruits"},
            "Milk": {"price": 48, "stock": 10, "discount": 0, "item_type": "Dairy"},
            "Bread": {"price": 28, "stock": 5, "discount": 0, "item_type": "Bakery"},
            "Orange": {"price": 15, "stock": 25, "discount": 10, "item_type": "Fruits"},
            "Cereal": {"price": 45, "stock": 12, "discount": 5, "item_type": "Breakfast"},
            "Yogurt": {"price": 28, "stock": 20, "discount": 0, "item_type": "Dairy"},
            "Onions": {"price": 18, "stock": 35, "discount": 0, "item_type": "Vegetables"},
            "Beef": {"price": 150, "stock": 8, "discount": 5, "item_type": "Meat"},
            "Coffee": {"price": 85, "stock": 15, "discount": 0, "item_type": "Beverages"},
        }
    },
    3: {
        "name": "Store C",
        "location": (4, 2),
        "manager": "manager3",
        "items": {
            "Apple": {"price": 11, "stock": 10, "discount": 0, "item_type": "Fruits"},
            "Orange": {"price": 14, "stock": 20, "discount": 5, "item_type": "Fruits"},
            "Milk": {"price": 47, "stock": 20, "discount": 5, "item_type": "Dairy"},
            "Cheese": {"price": 80, "stock": 10, "discount": 0, "item_type": "Dairy"},
            "Yogurt": {"price": 30, "stock": 15, "discount": 15, "item_type": "Dairy"},
            "Cookies": {"price": 40, "stock": 25, "discount": 10, "item_type": "Snacks"},
            "Chips": {"price": 25, "stock": 30, "discount": 0, "item_type": "Snacks"},
            "Lettuce": {"price": 22, "stock": 15, "discount": 0, "item_type": "Vegetables"},
            "Fish": {"price": 130, "stock": 12, "discount": 5, "item_type": "Seafood"},
            "Tea": {"price": 65, "stock": 18, "discount": 0, "item_type": "Beverages"},
        }
    }
}

orders = {}

# Generate unique order IDs
def generate_order_id():
    return "ORD-" + str(uuid4())[:8].upper()
