# Week 3 In-Class Exploration: Student Records Flask API

Build a Flask API for student records. This is the same data structure from Week 2 - now as a real HTTP API!

## The Transformation

Remember Week 2? You wrote functions like this:

```python
def get_student(student_id):
    student = students.get(student_id)
    if student is None:
        return {"error": "Student not found"}, 404
    return student, 200
```

This week, you add ONE line to make it a real API:

```python
@app.get('/students/<int:student_id>')
def get_student(student_id):
    student = students.get(student_id)
    if student is None:
        return {"error": "Student not found"}, 404
    return student, 200
```

**The function body is IDENTICAL!**

## Getting Started

```bash
# Clone this repository
git clone <your-repo-url>
cd in-class-exploration-week-3-<your-username>

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
flask run
```

## Your Task

Implement the endpoints in `app.py`. Each one is marked with a `TODO` comment.

### Data Structure

Students are stored as dictionaries (same as Week 2!):

```python
{
    "id": 1,
    "name": "Alice Smith",
    "email": "alice@berkeley.edu",
    "major": "Data Science"
}
```

### Endpoints to Implement

| Endpoint | Method | Description | Success | Error |
|----------|--------|-------------|---------|-------|
| `/students` | GET | List all students | `{"students": [...], "total": N}` | - |
| `/students/<id>` | GET | Get one student | student dict, 200 | `{"error": "..."}`, 404 |
| `/students` | POST | Create a student | new student, 201 | `{"error": "..."}`, 400 |
| `/students/<id>` | PUT | Update a student | updated student, 200 | `{"error": "..."}`, 404 |
| `/students/<id>` | DELETE | Delete a student | `{"message": "..."}`, 200 | `{"error": "..."}`, 404 |

### Testing Your API

Use the commands in `test-commands.sh` or run them manually:

```bash
# GET all students
curl http://localhost:5000/students

# GET one student
curl http://localhost:5000/students/1

# POST new student
curl -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "New Student", "email": "new@berkeley.edu", "major": "CS"}'

# PUT update student
curl -X PUT http://localhost:5000/students/1 \
  -H "Content-Type: application/json" \
  -d '{"major": "Machine Learning"}'

# DELETE student
curl -X DELETE http://localhost:5000/students/1
```

## Checkpoints

| Time | Goal |
|------|------|
| 0-5 min | Setup: clone, venv, pip install, flask run |
| 5-15 min | GET /students and GET /students/<id> |
| 15-25 min | POST /students with validation |
| 25-35 min | PUT /students/<id> and DELETE /students/<id> |
| 35-45 min | Extensions or polish |

## Tips

1. **Start with GET** - it's the simplest (no request body)
2. **Use `request.get_json()`** for POST/PUT to get the JSON body
3. **Check for None** - students.get() returns None if not found
4. **Return tuples** - `(data, status_code)` like `(student, 200)`
5. **Test often** - run curl after each endpoint

## Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: flask` | Activate venv: `source venv/bin/activate` |
| POST returns None | Add `-H "Content-Type: application/json"` to curl |
| 404 for everything | Check URL path matches decorator |
| Changes not showing | Restart Flask (or use `FLASK_DEBUG=1`) |

## Extensions (if you finish early)

1. **Search endpoint**: `GET /students?major=CS` - filter by major
2. **Pagination**: `GET /students?limit=10&offset=0`
3. **Validation**: Check email contains `@`
4. **Error handlers**: Custom JSON responses for 404, 400

## Submitting

At **10:45 AM**, commit and push:

```bash
git add .
git commit -m "In-class exploration submission"
git push
```

Then submit your repository URL on bCourses.

**Grading**: Pass/No Pass based on engagement. We're looking for evidence you worked on this for 30+ minutes.

**Want to keep working?** Continue after submitting and push your changes later!
