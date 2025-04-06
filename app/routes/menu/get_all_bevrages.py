from app.utils.project_imports import *





@app.get("/get/menu", tags=["Menu"])
def get_menu(request: Request, response: Response):
    try:
        get_recipes = recipe_collection.find()
        get_recipes = [serialize_recipe(r) for r in get_recipes]
        return {
            "message": "Successfully fetched menu.",
            "data": get_recipes
        }
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
