#!/usr/bin/env python3
"""
Week 2 In-Class Project: Student Records API

Implement the functions below to manage student records.
Each function follows the pattern you'll use with Flask next week.

Run tests with: python test_records.py
"""

import json

# =============================================================================
# DATA STORAGE
# =============================================================================
# Our in-memory "database" - a dictionary mapping student IDs to student data
students = {
    1: {"id": 1, "name": "Alice Smith", "email": "alice@berkeley.edu", "major": "Data Science"},
    2: {"id": 2, "name": "Bob Jones", "email": "bob@berkeley.edu", "major": "Computer Science"},
    3: {"id": 3, "name": "Carol White", "email": "carol@berkeley.edu", "major": "Information Systems"},
}

# Counter for generating new IDs
next_id = 4


# =============================================================================
# HELPER FUNCTIONS (already implemented for you)
# =============================================================================

def _get_next_id():
    """Get the next available student ID."""
    global next_id
    current_id = next_id
    next_id += 1
    return current_id


def print_json(data):
    """Pretty print data as JSON."""
    print(json.dumps(data, indent=2))


# =============================================================================
# TODO: IMPLEMENT THESE FUNCTIONS
# =============================================================================

def list_students():
    """
    Return all students.

    Returns:
        dict: {"students": [list of student dicts], "total": count}

    Example:
        >>> result = list_students()
        >>> print(result["total"])
        3
    """
    # TODO: Implement this function
    # Hint: Use list(students.values()) to get all student dicts
    # Hint: Use len() to count them
    all_students = list(students.values())
    return {
        "students": all_students,
        "total": len(all_students)
    }


def get_student(student_id):
    """
    Get a single student by ID.

    Args:
        student_id: The ID of the student to retrieve

    Returns:
        tuple: (student_dict, 200) if found
               ({"error": "Student not found"}, 404) if not found

    Example:
        >>> student, status = get_student(1)
        >>> print(status)
        200
        >>> print(student["name"])
        Alice Smith
    """
    # TODO: Implement this function
    # Hint: Use students.get(student_id) to safely get the student
    # Hint: Check if the result is None
    student = students.get(student_id)
    if student is None:
        return {"error": "Student not found"}, 404
    return student, 200


def add_student(data):
    """
    Add a new student.

    Args:
        data: Dictionary with student data (name, email, major)

    Returns:
        tuple: (new_student_dict, 201) if successful
               ({"error": "Missing required field: <field>"}, 400) if validation fails

    Required fields: name, email

    Example:
        >>> student, status = add_student({"name": "Dan", "email": "dan@berkeley.edu"})
        >>> print(status)
        201
    """
    # TODO: Implement this function
    # Step 1: Validate that 'name' is in data (return 400 error if not)
    if "name" not in data:
        return {"error": "Missing required field: name"}, 400
    
    # Step 2: Validate that 'email' is in data (return 400 error if not)
    if "email" not in data:
        return {"error": "Missing required field: email"}, 400

    # Step 3: Create new student dict with _get_next_id()
    new_id = _get_next_id()
    new_student = {
        "id": new_id,
        "name": data["name"],
        "email": data["email"],
        "major": data.get("major")
    }

    # Step 4: Add to students dictionary
    students[new_id] = new_student

    # Step 5: Return the new student and 201 status
    return new_student, 201


def update_student(student_id, data):
    """
    Update an existing student.

    Args:
        student_id: The ID of the student to update
        data: Dictionary with fields to update

    Returns:
        tuple: (updated_student_dict, 200) if successful
               ({"error": "Student not found"}, 404) if student doesn't exist

    Example:
        >>> student, status = update_student(1, {"major": "Machine Learning"})
        >>> print(student["major"])
        Machine Learning
    """
    # TODO: Implement this function
    # Step 1: Check if student exists (return 404 if not)
    if student_id not in students:
        return {"error": "Student not found"}, 404

    # Step 2: Update the student's fields with data
    # Hint: Use dict.update() to merge data into the student
    # Hint: Don't allow changing the ID
    student = students[student_id]
    
    # Create a copy of data to avoid modifying the input or adding 'id' if passed
    update_data = data.copy()
    update_data.pop("id", None)  # Ensure ID doesn't change
    
    student.update(update_data)

    # Step 3: Return the updated student and 200 status
    return student, 200


def delete_student(student_id):
    """
    Delete a student.

    Args:
        student_id: The ID of the student to delete

    Returns:
        tuple: ({"message": "Student deleted"}, 200) if successful
               ({"error": "Student not found"}, 404) if student doesn't exist

    Example:
        >>> result, status = delete_student(1)
        >>> print(status)
        200
    """
    # TODO: Implement this function
    # Hint: Use students.pop(student_id, None) to remove and check if existed
    deleted_student = students.pop(student_id, None)
    
    if deleted_student is None:
        return {"error": "Student not found"}, 404
        
    return {"message": "Student deleted"}, 200


# =============================================================================
# OPTIONAL: STUDENT CLASS
# =============================================================================
# If you finish early, refactor to use this class

class Student:
    """
    A Student class with JSON serialization.

    This is optional but shows the pattern used in SQLAlchemy models.
    """

    def __init__(self, id, name, email, major=None):
        # TODO (optional): Add validation
        # - name must be at least 2 characters
        # - email must contain @
        self.id = id
        self.name = name
        self.email = email
        self.major = major

    def to_dict(self):
        """Convert to dictionary for JSON serialization."""
        # TODO (optional): Implement this method
        pass

    @classmethod
    def from_dict(cls, data, id=None):
        """Create a Student from a dictionary."""
        # TODO (optional): Implement this method
        pass


# =============================================================================
# MAIN - for testing individual functions
# =============================================================================

if __name__ == "__main__":
    print("Student Records API - Manual Testing")
    print("=" * 50)

    # Test list_students
    print("\n1. List all students:")
    result = list_students()
    if result:
        print_json(result)
    else:
        print("   Not implemented yet")

    # Test get_student
    print("\n2. Get student with ID 1:")
    result = get_student(1)
    if result:
        student, status = result
        print(f"   Status: {status}")
        print_json(student)
    else:
        print("   Not implemented yet")

    # Test get_student (not found)
    print("\n3. Get student with ID 99 (should be 404):")
    result = get_student(99)
    if result:
        data, status = result
        print(f"   Status: {status}")
        print_json(data)
    else:
        print("   Not implemented yet")

    # Test add_student
    print("\n4. Add new student:")
    result = add_student({"name": "Dan Brown", "email": "dan@berkeley.edu", "major": "Statistics"})
    if result:
        student, status = result
        print(f"   Status: {status}")
        print_json(student)
    else:
        print("   Not implemented yet")

    # Test update_student
    print("\n5. Update student 1's major:")
    result = update_student(1, {"major": "Machine Learning"})
    if result:
        student, status = result
        print(f"   Status: {status}")
        print_json(student)
    else:
        print("   Not implemented yet")

    # Test delete_student
    print("\n6. Delete student 2:")
    result = delete_student(2)
    if result:
        data, status = result
        print(f"   Status: {status}")
        print_json(data)
    else:
        print("   Not implemented yet")

    # Final state
    print("\n7. Final list of students:")
    result = list_students()
    if result:
        print_json(result)
    else:
        print("   Not implemented yet")
