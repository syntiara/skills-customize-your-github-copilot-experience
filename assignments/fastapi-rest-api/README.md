# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, fast REST APIs using the FastAPI framework. You'll create a fully functional API with endpoints for managing resources, implement request validation, and understand HTTP methods and status codes.

## 📝 Tasks

### 🛠️ Build a Todo API

#### Description
Create a REST API for managing a todo list using FastAPI. The API should allow users to create, read, update, and delete todo items with proper error handling and data validation.

#### Requirements
Completed API should:

- Accept POST requests to create new todo items with title and description
- Accept GET requests to retrieve all todos or a specific todo by ID
- Accept PUT requests to update existing todo items
- Accept DELETE requests to remove todo items
- Return appropriate HTTP status codes (200, 201, 404, etc.)
- Validate input data using Pydantic models
- Include error handling with meaningful error messages


### 🛠️ Add Advanced Features

#### Description
Extend your API with more sophisticated features including filtering, sorting, and status tracking for improved functionality.

#### Requirements
Completed API should:

- Support filtering todos by status (pending, completed)
- Support sorting todos by creation date or priority
- Track todo completion status with a boolean field
- Return paginated results for large lists
- Include request/response examples in API documentation
- Use Pydantic models for all data validation
