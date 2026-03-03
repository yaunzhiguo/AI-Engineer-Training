# Day03 - FastAPI Student CRUD API

## 📌 Project Overview

This project builds a RESTful Student Management API using FastAPI.

It reuses the service layer from Day02 and exposes CRUD operations via HTTP endpoints.

## 🏗 Architecture

- FastAPI (API Layer)
- Router-based modular structure
- Service Layer (Reused from Day02)
- Pydantic for request validation
- Dependency Injection (Depends)
- JSON-based persistence (temporary storage)

## 📂 Project Structure

day03/
└── app/
├── main.py
├── schemas.py
├── dependencies.py (optional)
└── routers/
└── students.py


## 🚀 How to Run

Activate virtual environment first:

```bash
venv\Scripts\activate
Then start server:
python -m uvicorn day03.app.main:app --reload --reload-dir day03 --host 127.0.0.1 --port 8000
Open Swagger UI:http://127.0.0.1:8000/docs

## 📡 API Endpoints

GET /health

GET /students

GET /students/{name}

POST /students

PUT /students/{name}

DELETE /students/{name}

###
✅ Features Implemented

RESTful API design

HTTP status code handling (200 / 201 / 404 / 409 / 422)

Pydantic validation

Dependency Injection

Router modularization

Pagination

Custom validation error handling

🎯 Learning Goals

Build structured backend API

Understand request validation and status codes

Implement service layer reuse

Practice modular backend architecture
