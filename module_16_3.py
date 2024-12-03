from fastapi import FastAPI, HTTPException, Path
from typing import Annotated

app = FastAPI()

users = {"1": 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_all_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[str, Path(min_length=1, max_length=50, description='Введите имя пользователя', example='ExampleUser')],
    age: Annotated[int, Path(ge=0, le=120, description='Введите возраст', example=25)]
) -> str:
    current_key = str(int(max(users, key=int)) + 1)
    users[current_key] = f'Имя: {username}, возраст: {age}'
    return f"User {current_key} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[str, Path(description='ID пользователя для обновления', example='1')],
    username: Annotated[str, Path(min_length=1, max_length=50, description='Введите имя пользователя', example='UpdatedUser')],
    age: Annotated[int, Path(ge=0, le=120, description='Введите возраст', example=30)]
) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[str, Path(description='ID пользователя для удаления', example='1')]) -> str:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users.pop(user_id)
    return f'User {user_id} was deleted'
