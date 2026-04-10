from fastapi import FastAPI
from app.database import Base, engine
from app.routes import task as task_routes
import uvicorn
app = FastAPI(title="Task Manager API")

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}


app.include_router(task_routes.router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
