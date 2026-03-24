from fastapi import FastAPI
from app.database import Base, engine
from app.routes import task as task_routes

app = FastAPI(title="Task Manager API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}


app.include_router(task_routes.router)