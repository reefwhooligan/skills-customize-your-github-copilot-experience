# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build RESTful APIs using the FastAPI framework. You'll create a web service that handles HTTP requests and returns JSON responses, mastering core API concepts like routes, request/response handling, and data validation.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Application

#### Description
Build a basic FastAPI application with multiple routes that demonstrate different HTTP methods and response types.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Define at least 3 routes using different HTTP methods (GET, POST, PUT, or DELETE)
- Return JSON responses from each route
- Include proper status codes (200 for success, 404 for not found, etc.)
- Test the API using the auto-generated documentation at `/docs`

### 🛠️ Implement Data Validation and Models

#### Description
Extend your API to use Pydantic models for request/response data validation and ensure type safety.

#### Requirements
Completed program should:

- Define at least 2 Pydantic models for data structures
- Use models in route functions for request body validation
- Return model instances from API endpoints
- Handle validation errors gracefully with appropriate error messages
- Demonstrate creating, reading, and updating data with validated models
