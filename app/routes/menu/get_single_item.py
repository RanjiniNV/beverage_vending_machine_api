from app.utils.project_imports import *


@app.get("/get/ingredients/{beverage_name}", tags=["Menu"])
def get_menu(request: Request, response: Response, beverage_name: str):
    try:
        get_recipes = (recipe_collection.find_one({"name": beverage_name}, {"_id": 0}))
        if not get_recipes:
            response.status_code = 400
            return {
                "message": f"{beverage_name} not in menu."
            }
        return {
            "message": f"Successfully fetched {beverage_name} ingredients.",
            "data": get_recipes['ingredients']
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
