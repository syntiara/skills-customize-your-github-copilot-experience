"""
FastAPI Todo API Starter Code

This file provides a basic structure for building a REST API with FastAPI.
Complete the implementation following the assignment requirements.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# TODO: Define Pydantic models for request/response data
# Example: TodoItem, TodoCreate, etc.

# TODO: Create an in-memory data store (list or dictionary)
# to store todo items

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Todo API"}


# TODO: Implement the following endpoints:
# POST /todos - Create a new todo
# GET /todos - Get all todos (with optional filtering/sorting)
# GET /todos/{todo_id} - Get a specific todo
# PUT /todos/{todo_id} - Update a todo
# DELETE /todos/{todo_id} - Delete a todo

# Hints:
# - Use Pydantic models for validation
# - Return appropriate HTTP status codes
# - Handle missing resources with 404 errors
# - Add docstrings to each endpoint
