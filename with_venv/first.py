from fastapi import FastAPI

app = FastAPI()

# Home page 
@app.get("/")
def home():
    return {"Welcome to Home Page"}

# About Route
@app.get("/about")
def about():
    return {"welcome to About Page"}

# Users route
@app.get("/users")
def users():
    return  {
        "users" : ["mohit","Amit","rohit"]
    }