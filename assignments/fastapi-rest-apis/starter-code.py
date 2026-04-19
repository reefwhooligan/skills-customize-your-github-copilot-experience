"""
Starter code for Building REST APIs with FastAPI assignment.
Complete the tasks by implementing the required routes and models.
"""

from fastapi import FastAPI
from pydantic import BaseModel

# Initialize the FastAPI application
app = FastAPI()

# TODO: Define Pydantic models for data validation
# Example: Create a model for representing a resource (e.g., Item, User, Task)


# TODO: Implement your routes here
# Example:
# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int):
#     return {"item_id": item_id}

# @app.post("/items/")
# def create_item(item: YourModel):
#     return item


if __name__ == "__main__":
    # Run with: uvicorn starter-code:app --reload
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
