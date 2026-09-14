# Student Management API

## Project 2 - Backend API Development

This project is a professional backend REST API built with Python and Flask to demonstrate core backend/server-side development concepts.

## Objective

The application is designed to:

- Handle GET requests for reading data
- Handle POST requests for creating new records
- Accept and process user input
- Return structured JSON responses
- Validate incoming data on the server side
- Use proper HTTP status codes for success and error handling

## Technologies Used

- Python
- Flask
- Flask-CORS
- REST API design
- JSON-based communication

## Features

- Fetch all students
- Fetch a student by ID
- Add a new student
- Input validation for name, age, and course
- Friendly JSON responses for both success and error cases
- Server-side logic that simulates a basic academic record system

## API Endpoints

### 1. Home

Method: GET
URL: http://127.0.0.1:5000/

### 2. Health Check

Method: GET
URL: http://127.0.0.1:5000/health

### 3. Get All Students

Method: GET
URL: http://127.0.0.1:5000/students

### 4. Get Student by ID

Method: GET
URL: http://127.0.0.1:5000/students/1

### 5. Add Student

Method: POST
URL: http://127.0.0.1:5000/students

Example request body:

{
  "name": "Ananya",
  "age": 20,
  "course": "Artificial Intelligence"
}

## Validation Rules

The API validates:

- Name is required and cannot be empty
- Age must be a valid integer between 1 and 120
- Course is required and cannot be empty
- JSON body must be present and valid
- Student ID must exist when fetching a single record

## HTTP Status Codes

- 200: Successful GET request
- 201: Student successfully created
- 400: Invalid request or validation error
- 404: Student not found
- 405: Unsupported HTTP method

## How to Run

1. Open a terminal in the project folder.
2. Install dependencies:
   pip install -r requirements.txt
3. Start the Flask API:
   python app.py
4. Access the application at:
   http://127.0.0.1:5000/

## Example Response

Success response for GET /students:

{
  "success": true,
  "count": 2,
  "students": [
    {"id": 1, "name": "Rahul", "age": 20, "course": "Computer Science"},
    {"id": 2, "name": "Priya", "age": 21, "course": "Information Technology"}
  ]
}

Error response example:

{
  "success": false,
  "error": "Age must be a valid integer between 1 and 120"
}