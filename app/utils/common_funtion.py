import pytz

from app.utils.common_imports import *
def serialize_recipe(recipe):
    recipe.pop("_id", None)
    return recipe

def get_ist_ts():
    ist = pytz.timezone("Asia/Kolkata")
    return datetime.now(ist)