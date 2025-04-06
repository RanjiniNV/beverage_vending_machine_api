from app.utils.project_imports import *
from app.models import new_recipe


@app.post("/add/recipe", tags=["Recipe"])
def order_your_drink(request: Request, response: Response, new_recipe: new_recipe):
    try:
        if recipe_collection.find_one({"name": new_recipe.name}):
            response.status_code = 400
            return {"message": "Recipe with this name already exists"}
        new_recipe = new_recipe.dict()
        name = new_recipe["name"]
        new_recipe.pop("name", None)
        recipe_collection.insert_one({"name": name, "ingredients": new_recipe})
        return {"message": f"{name} added to menu."}
    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
