# Week 2 In-Class Project: Student Records API

Build Python functions that manage student records. These functions follow the exact pattern you'll use with Flask next week!

## Getting Started

```bash
# Clone this repository
git clone <your-repo-url>

# Navigate to the cloned folder
cd in-class-exploration-week-2-<your-username>

# Open in your editor
code .

# Run tests to see what needs to be implemented
python test_records.py
```

## Your Task

Implement the functions in `student_records.py`. Each function is marked with a `TODO` comment.

### Data Structure

Students are stored as dictionaries with these fields:

```python
{
    "id": 1,
    "name": "Alice Smith",
    "email": "alice@berkeley.edu",
    "major": "Data Science"
}
```

### Functions to Implement

| Function | Description | Returns |
|----------|-------------|---------|
| `list_students()` | Get all students | `{"students": [...], "total": N}` |
| `get_student(id)` | Get one student by ID | `(student_dict, 200)` or `(error, 404)` |
| `add_student(data)` | Create a new student | `(student_dict, 201)` or `(error, 400)` |
| `update_student(id, data)` | Update existing student | `(student_dict, 200)` or `(error, 404)` |
| `delete_student(id)` | Remove a student | `(message, 200)` or `(error, 404)` |

### Response Pattern

All functions that can fail return a tuple of `(data, status_code)`:

```python
# Success
return {"id": 1, "name": "Alice"}, 200

# Not found
return {"error": "Student not found"}, 404

# Bad request
return {"error": "Missing required field: name"}, 400
```

## Checkpoints

Use these time targets to pace yourself:

| Time | Checkpoint |
|------|------------|
| 0-10 min | Implement `list_students()` and `get_student()` |
| 10-20 min | Implement `add_student()` with validation |
| 20-30 min | Implement `update_student()` and `delete_student()` |
| 30-40 min | Create a `Student` class with `to_dict()` (optional) |
| 40-45 min | Add custom features, run all tests |

## Running Tests

```bash
python test_records.py
```

The test script will show which functions pass and which need work.

## Tips

1. **Start simple:** Get the basic version working, then add validation
2. **Use `.get()`:** Safely access dictionary keys: `students.get(id)` returns `None` if not found
3. **Check tests often:** Run tests after each function to verify
4. **Read the error messages:** Python's error messages tell you exactly what's wrong

## Common Issues

| Issue | Solution |
|-------|----------|
| `KeyError` | Use `.get()` instead of direct access, or check if key exists |
| `TypeError: 'NoneType'` | You're accessing something that's `None` - add a check |
| Test says "not implemented" | You have a `pass` or `TODO` still in the function |

## Extensions (if you finish early)

1. Add a `search_students(query)` function that finds students by name
2. Add validation for email format (must contain `@`)
3. Add a `major` filter to `list_students()`
4. Implement the `Student` class with validation in `__init__`

## Submitting

At **10:45 AM PST**, the instructor will ask you to:

1. **Commit** everything you have (even if incomplete):
   ```bash
   git add .
   git commit -m "In-class exploration submission"
   ```

2. **Push** to your repository:
   ```bash
   git push
   ```

3. **Submit on bCourses**: Go to the In-Class Exploration assignment and submit the URL to your GitHub repository homepage. It should look something like:
   ```
   https://github.com/UCB-INFO-BACKEND-WEBARCH/in-class-exploration-week-2-yourusername
   ```

**Remember:** This is graded Pass/No Pass on engagement, not correctness! The instructor is just looking for evidence that you actually worked on this for the past 30+ minutes.

**Want to keep working?** Feel free to continue after submitting! Just commit and push your additional changes whenever you're done.
