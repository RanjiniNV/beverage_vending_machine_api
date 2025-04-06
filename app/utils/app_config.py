from app.utils.common_imports import *

app = FastAPI(
    title="Beverage Vending Machine API",
    description="This API allows you to interact with the vending machine – get beverages, manage recipes, and track "
                "inventory.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
    openapi_url="/openapi.json"
)


