from fastapi import FastAPI
from routes.task import router as task_router
from routes.user import router as user_router

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# Подключение маршрутов
app.include_router(task_router)
app.include_router(user_router)
