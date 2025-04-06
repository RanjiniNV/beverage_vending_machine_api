from app.utils.common_imports import *

client = MongoClient("mongodb://localhost:27017/")

db = client["vending_db"]
inventory_collection = db["inventory"]
recipe_collection = db["recipes"]
order_collection = db["orders"]