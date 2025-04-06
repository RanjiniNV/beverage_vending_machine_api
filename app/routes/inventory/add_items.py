from app.utils.project_imports import *
from app.models import inventory_items


@app.post("/add/item", tags=["Inventory"])
def add_items(request: Request, response: Response, items: inventory_items):
    try:
        items = items.dict()
        for each in Ing:
            inventory_response = inventory_collection.update_one({"_id": each},
                                                                 {"$inc": {"quantity": items[each]}})
        return {"message": "Inventory filled successfully."}

    except Exception as error:
        raise HTTPException(status_code=500, detail=str(error))
