#!/usr/bin/env python3
"""
Week 3 In-Class Exploration: Student Records Flask API

Transform your Week 2 Python functions into a real Flask API!
The function bodies are the same - just add the decorators.
"""

from flask import Flask, request

app = Flask(__name__)

# =============================================================================
# DATA STORAGE (same structure from Week 2!)
# =============================================================================

students = {
    1: {"id": 1, "name": "Alice Smith", "email": "alice@berkeley.edu", "major": "Data Science"},
    2: {"id": 2, "name": "Bob Jones", "email": "bob@berkeley.edu", "major": "Computer Science"},
    3: {"id": 3, "name": "Carol White", "email": "carol@berkeley.edu", "major": "Information Systems"},
}

next_id = 4


# =============================================================================
# API ENDPOINTS - Implement these!
# =============================================================================

# TODO 1: GET /students - List all students
# Should return: {"students": [...], "total": N}
# Hint: list(students.values()) gives you all students
@app.get('/students')
def list_students():
    all_students = list(students.values())
    return {"students": all_students, "total": len(all_students)}


# TODO 2: GET /students/<id> - Get one student
# Should return: student dict with 200, or {"error": "Student not found"} with 404
# Hint: students.get(student_id) returns None if not found
@app.get('/students/<int:student_id>')
def get_student(student_id):
    student = students.get(student_id)
    if student:
        return student
    return {"error": "Student not found"}, 404


# TODO 3: POST /students - Create a new student
# Should:
#   - Get JSON data with request.get_json()
#   - Validate that "name" is provided (return 400 if not)
#   - Create new student with next available ID
#   - Return new student with 201
# Hint: Use global next_id and increment it
@app.post('/students')
def create_student():
    global next_id
    data = request.get_json()
    if not data or "name" not in data:
        return {"error": "Student name is required"}, 400
    
    new_student = {
        "id": next_id,
        "name": data["name"],
        "email": data.get("email", ""),
        "major": data.get("major", "Intended")
    }
    students[next_id] = new_student
    next_id += 1
    return new_student, 201


# TODO 4: PUT /students/<id> - Update a student
# Should:
#   - Check if student exists (return 404 if not)
#   - Get JSON data with request.get_json()
#   - Update the student's fields (don't allow changing ID)
#   - Return updated student with 200
@app.put('/students/<int:student_id>')
def update_student(student_id):
    if student_id not in students:
        return {"error": "Student not found"}, 404
    
    data = request.get_json()
    student = students[student_id]
    
    # Update fields if provided
    if "name" in data:
        student["name"] = data["name"]
    if "email" in data:
        student["email"] = data["email"]
    if "major" in data:
        student["major"] = data["major"]
        
    return student


# TODO 5: DELETE /students/<id> - Delete a student
# Should:
#   - Check if student exists (return 404 if not)
#   - Remove student from storage
#   - Return {"message": "Student deleted"} with 200
# Hint: students.pop(student_id, None) removes and returns, or None if not found
@app.delete('/students/<int:student_id>')
def delete_student(student_id):
    student = students.pop(student_id, None)
    if not student:
        return {"error": "Student not found"}, 404
        
    return {"message": "Student deleted"}


# =============================================================================
# EXTENSIONS (optional - if you finish early)
# =============================================================================

# EXTENSION 1: Search/filter students
# GET /students?major=CS should return only CS students
# Hint: Use request.args.get('major') to get query parameter


# EXTENSION 2: Pagination
# GET /students?limit=10&offset=0
# Hint: Use request.args.get('limit', default=10, type=int)


# =============================================================================
# RUN THE APP
# =============================================================================


# need to use port 5001 because apparently macOS AirPlay Receiver uses port 5000 so I had trouble
if __name__ == '__main__':
    app.run(debug=True, port=5001)
