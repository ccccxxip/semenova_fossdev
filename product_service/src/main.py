from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI(title="Product Service", version="0.1.0")


class Product(BaseModel):
    id: str
    name: str
    price: float
    available: bool

products_db: Dict[str, Product] = {
    "pencil": Product(id="pencil", name="Pencil", price=1.50, available=True),
    "notebook": Product(id="notebook", name="Notebook", price=4.20, available=True),
    "backpack": Product(id="backpack", name="Backpack", price=35.00, available=False),
    "laptop": Product(id="laptop", name="Laptop", price=1200.00, available=True),
    "mouse": Product(id="mouse", name="Mouse", price=25.50, available=True),
    "keyboard": Product(id="keyboard", name="Keyboard", price=75.00, available=False),
}


@app.get("/")
def root() -> dict:
    return {"service": "product_service", "status": "ok"}


@app.get("/health")
def health() -> dict:
    return {"status": "healthy", "service": "product-service"}


@app.get("/products")
def list_products() -> List[Product]:
    return list(products_db.values())


@app.get("/products/{product_id}")
def get_product(product_id: str) -> Product:
    if product_id not in products_db:
        raise HTTPException(
            status_code=404,
            detail=f"Product '{product_id}' was not found",
        )
    return products_db[product_id]
