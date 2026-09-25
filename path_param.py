from fastapi import FastAPI

app = FastAPI()

# dynamic route with data type
@app.get("/users/{user_id}")
def get_users(user_id: int):
    return {
        "user_id": user_id,
        "users": ["sunil", "smay", "ajit"]
    }
