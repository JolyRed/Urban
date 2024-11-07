from fastapi import FastAPI, Body, status, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int = None
    username: str
    age: int

users = []

@app.get("/users")
async def get_all_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}")
async def create_user(user: User, username: str, age: int) -> User:
    new_id = 1 if not users else max(user.id for user in users) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: int, username: str, age: str) -> User:
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    user.username = username
    user.age = age
    return user


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> User:
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    users.remove(user)
    return user
