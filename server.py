from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: str


@app.get("/")
def main():
    print("hi")
    return {"status": "API Online."}

@app.post("/products/")
def add_product(product: Product):
    print(product)
    return {"status": "product added successfully."}
