from fastapi import FastAPI

app = FastAPI()


products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 50000,
        "category": "Electronics"
    },
    {
        "id": 2,
        "name": "Mobile",
        "price": 25000,
        "category": "Electronics"
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 1500,
        "category": "Accessories"
    }
]


@app.get("/")
def home():
    return {
        "message": "Welcome to Product API"
    }


@app.get("/products")
def get_products():
    return {
        "products": products
    }


@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:

        if product["id"] == product_id:
            return product

    return {
        "message": "Product not found"
    }