from app.routes.inventory.add_items import *
from app.routes.orders.order_bevrage import *
from app.routes.menu.get_all_bevrages import *
from app.routes.menu.get_single_item import *
from app.routes.recipe.add_new_recipe import *
from app.routes.recipe.add_new_recipe import *
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", port=8009, host="localhost", log_level="info", reload=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
