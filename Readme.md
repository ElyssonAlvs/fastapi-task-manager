# 🚀 FastAPI Task Manager API

A simple and well-structured Task Manager API built with FastAPI.
This project demonstrates backend fundamentals such as API structure, database integration, and clean architecture.

---

## 📌 Features

- ✅ Create tasks (`POST /tasks/`)
- ✅ List tasks with pagination and status filtering (`GET /tasks/`)
- ✅ Retrieve, update, and delete tasks by ID
- ✅ Status management (pending, done, in_progress)
- ✅ Input validation with Pydantic and field constraints
- ✅ Type hints with `Annotated` (FastAPI best practices)
- ✅ Database session handling with `Depends`
- ✅ Automatic API documentation (Swagger & ReDoc)

---

## 🧱 Tech Stack

- Python 3.10+
- FastAPI (with modern best practices)
- SQLAlchemy ORM
- Pydantic (data validation)
- SQLite
- Uvicorn (ASGI server)
- Pytest (testing)

---

## 📂 Project Structure

```
app/
 ├── __init__.py
 ├── main.py
 ├── database.py
 ├── models/
 │   ├── __init__.py
 │   └── task.py
 ├── schemas/
 │   ├── __init__.py
 │   └── task.py
 └── routes/
     ├── __init__.py
     └── task.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/fastapi-task-manager.git
cd fastapi-task-manager
```

### 2. Create virtual environment

```
python -m venv venv
```

Activate:

- Windows:

```
venv\Scripts\activate
```

- Linux/Mac:

```
source venv/bin/activate
```

### 3. Install dependencies

```
pip install fastapi uvicorn sqlalchemy pydantic
```

> Do not use `pip install app`, `pip install task`, or `pip install app.*`.
> Those commands install packages from PyPI and can break local dependencies.

---

## ▶️ Running the project

```
uvicorn app.main:app --reload
```

---

## 📖 API Documentation

Once running, access:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🗄️ Database

- SQLite database (`tasks.db`) is created automatically
- Managed via SQLAlchemy ORM

---

## 📌 API Endpoints

### Tasks


| Method | Endpoint | Description                | Status      |
| ------ | -------- | -------------------------- | ----------- |
| POST   | /tasks/  | Create a new task          | ✅ Implemented |
| GET    | /tasks/  | List tasks with filters    | ✅ Implemented |
| GET    | /tasks/{id} | Get task by ID          | ✅ Implemented |
| PUT    | /tasks/{id} | Update a task           | ✅ Implemented |
| DELETE | /tasks/{id} | Delete a task           | ✅ Implemented |


---

## 🔍 Query Parameters

- `status` -> filter by status (`pending`, `done`) - optional
- `skip` -> pagination offset (default: 0, min: 0)
- `limit` -> pagination limit (default: 10, max: 100)

Examples:

```
/tasks                                    # list all tasks
/tasks?status=pending                     # list pending tasks
/tasks?status=done&skip=0&limit=10        # list done tasks with pagination
/tasks?skip=20&limit=5                    # pagination only
```

---

## 🧠 Learning Goals

This project focuses on:

- REST API design
- Clean code organization
- Database integration
- Data validation with Pydantic
- Backend best practices

---

## 🚀 Future Improvements

- Authentication (JWT)
- Docker support
- Comprehensive unit tests with Pytest
- PostgreSQL integration
- Request logging and monitoring
- Rate limiting
- API versioning
- Deployment to cloud (Heroku, AWS, etc.)

---

## 👨‍💻 Author

Developed by Elysson Alves
