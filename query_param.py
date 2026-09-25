from fastapi import FastAPI

app = FastAPI()

# query param - filtering , searching and sorting
# /users?name=mohit
# /products?price=1000
# http://127.0.0.1:8000/users?name=ajit
# 1. optional param
# 2. default param  
# 3. multiple query params


# if  http://127.0.0.1:8000/users enter then error not happen if value not provide 
# then default none will consider 

# @app.get("/users")
# def get_users(name : str = None):
#     return {"Name ":name}


# 2. default param  
# @app.get("/products")
# def get_products(limit : int = 10):
#     return {"limit":limit}

# 3. multiple query params
# http://127.0.0.1:8000/items?name=laptop&price=10000
@app.get("/items")
def get_items(name : str = None , price : int = 0):
    return {
        "name":name,
        "price":price
    }