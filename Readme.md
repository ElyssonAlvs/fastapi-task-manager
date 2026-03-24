# 🚀 FastAPI Task Manager API

A simple and well-structured Task Manager API built with FastAPI.
This project demonstrates backend fundamentals such as CRUD operations, database integration, filtering, and clean architecture.

---

## 📌 Features

- Create tasks
- List all tasks
- Get task by ID
- Update tasks
- Delete tasks
- Filter tasks by status
- Pagination support
- Automatic API documentation (Swagger)

---

## 🧱 Tech Stack

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

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

## 📌 API Endpoints (planned)

### Tasks


| Method | Endpoint    | Description       |
| ------ | ----------- | ----------------- |
| POST   | /tasks      | Create a new task |
| GET    | /tasks      | List all tasks    |
| GET    | /tasks/{id} | Get task by ID    |
| PUT    | /tasks/{id} | Update a task     |
| DELETE | /tasks/{id} | Delete a task     |


---

## 🔍 Query Parameters (planned)

- `status` → filter tasks (pending, done)
- `skip` → pagination offset
- `limit` → pagination limit

Example:

```
/tasks?status=pending&skip=0&limit=10
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
- Unit tests with Pytest
- PostgreSQL integration
- Deployment

---

## 👨‍💻 Author

Developed by Elysson Alves