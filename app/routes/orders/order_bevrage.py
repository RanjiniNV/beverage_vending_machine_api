import datetime

from app.utils.project_imports import *


@app.post("/order/{beverage_name}", tags=["Order"])
def order_your_drink(request: Request, response: Response, beverage_name: str):
    try:
        order_id = order_collection.insert_one({"beverage_name": beverage_name,
                                                "order_processed": False,
                                                "order_given_ts": datetime.now()
                                                })
        get_recipe = (recipe_collection.find_one({"name": beverage_name}))
        if not get_recipe:
            response.status_code = 400
            return {"message": f"{beverage_name} not in recipes.Got to menu to check the recipe"}
        check_ingredient = get_recipe.get("ingredients")
        check_inventory = list(inventory_collection.find())
        check_inventory = {each['_id']: each['quantity'] for each in check_inventory}
        for ingredient, quantity in check_ingredient.items():
            if not ingredient in check_inventory:
                response.status_code = 400
                return {"message": f"{ingredient} not in inventory."}
            if not check_inventory[ingredient] >= quantity:
                response.status_code = 400
                return {"message": f"{ingredient} is not sufficient for {beverage_name},please add {ingredient} to "
                                   f"continue with {beverage_name} orders."}
            inventory_collection.update_one({"_id": ingredient}, {
                "$inc": {"quantity": -quantity}
            })
            order_collection.update_one({"_id": order_id.inserted_id}, {
                "$set": {
                    "order_processed": True,
                    "order_processed_ts": datetime.now()
                }
            })
        return {"message": f"{beverage_name} dispensed successfully!"}
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
