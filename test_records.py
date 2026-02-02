#!/usr/bin/env python3
"""
Test script for Week 2 In-Class Project: Student Records API

Run this to check your implementation:
    python test_records.py
"""

import sys
from student_records import (
    list_students,
    get_student,
    add_student,
    update_student,
    delete_student,
    students,
)


def reset_data():
    """Reset the students data to initial state."""
    global students
    students.clear()
    students.update({
        1: {"id": 1, "name": "Alice Smith", "email": "alice@berkeley.edu", "major": "Data Science"},
        2: {"id": 2, "name": "Bob Jones", "email": "bob@berkeley.edu", "major": "Computer Science"},
        3: {"id": 3, "name": "Carol White", "email": "carol@berkeley.edu", "major": "Information Systems"},
    })


class TestResult:
    def __init__(self, name):
        self.name = name
        self.passed = 0
        self.failed = 0
        self.errors = []

    def ok(self, message):
        self.passed += 1
        print(f"  [PASS] {message}")

    def fail(self, message, expected=None, got=None):
        self.failed += 1
        error_msg = f"  [FAIL] {message}"
        if expected is not None:
            error_msg += f"\n         Expected: {expected}"
            error_msg += f"\n         Got: {got}"
        print(error_msg)
        self.errors.append(message)


def test_list_students():
    """Test the list_students function."""
    result = TestResult("list_students")
    reset_data()

    print("\nTesting list_students()...")

    # Test: returns a dictionary
    response = list_students()
    if response is None:
        result.fail("Function returns None - not implemented yet")
        return result

    if not isinstance(response, dict):
        result.fail("Should return a dictionary", "dict", type(response).__name__)
        return result
    result.ok("Returns a dictionary")

    # Test: has 'students' key
    if "students" not in response:
        result.fail("Response should have 'students' key")
        return result
    result.ok("Has 'students' key")

    # Test: has 'total' key
    if "total" not in response:
        result.fail("Response should have 'total' key")
    else:
        result.ok("Has 'total' key")

    # Test: students is a list
    if not isinstance(response.get("students"), list):
        result.fail("'students' should be a list")
        return result
    result.ok("'students' is a list")

    # Test: correct count
    if response.get("total") == 3:
        result.ok("Correct total count (3)")
    else:
        result.fail("Incorrect total count", 3, response.get("total"))

    # Test: students have required fields
    if len(response["students"]) > 0:
        student = response["students"][0]
        required = ["id", "name", "email"]
        has_all = all(field in student for field in required)
        if has_all:
            result.ok("Students have required fields (id, name, email)")
        else:
            result.fail("Students missing required fields", required, list(student.keys()))

    return result


def test_get_student():
    """Test the get_student function."""
    result = TestResult("get_student")
    reset_data()

    print("\nTesting get_student()...")

    # Test: get existing student
    response = get_student(1)
    if response is None:
        result.fail("Function returns None - not implemented yet")
        return result

    if not isinstance(response, tuple) or len(response) != 2:
        result.fail("Should return (data, status_code) tuple", "tuple of length 2", type(response).__name__)
        return result
    result.ok("Returns (data, status_code) tuple")

    student, status = response

    if status == 200:
        result.ok("Returns 200 for existing student")
    else:
        result.fail("Should return 200 for existing student", 200, status)

    if isinstance(student, dict) and student.get("name") == "Alice Smith":
        result.ok("Returns correct student data")
    else:
        result.fail("Should return Alice Smith", "Alice Smith", student.get("name") if isinstance(student, dict) else student)

    # Test: get non-existent student
    response = get_student(999)
    if response is not None:
        data, status = response
        if status == 404:
            result.ok("Returns 404 for non-existent student")
        else:
            result.fail("Should return 404 for non-existent student", 404, status)

        if isinstance(data, dict) and "error" in data:
            result.ok("Returns error message for non-existent student")
        else:
            result.fail("Should return error dict for non-existent student")

    return result


def test_add_student():
    """Test the add_student function."""
    result = TestResult("add_student")
    reset_data()

    print("\nTesting add_student()...")

    # Test: add valid student
    new_student_data = {"name": "Dan Brown", "email": "dan@berkeley.edu", "major": "Statistics"}
    response = add_student(new_student_data)

    if response is None:
        result.fail("Function returns None - not implemented yet")
        return result

    if not isinstance(response, tuple) or len(response) != 2:
        result.fail("Should return (data, status_code) tuple")
        return result
    result.ok("Returns (data, status_code) tuple")

    student, status = response

    if status == 201:
        result.ok("Returns 201 for created student")
    else:
        result.fail("Should return 201 for created student", 201, status)

    if isinstance(student, dict) and student.get("name") == "Dan Brown":
        result.ok("Returns created student data")
    else:
        result.fail("Should return created student")

    if isinstance(student, dict) and "id" in student:
        result.ok("Created student has an ID")
    else:
        result.fail("Created student should have an ID")

    # Test: missing name
    response = add_student({"email": "test@berkeley.edu"})
    if response is not None:
        data, status = response
        if status == 400:
            result.ok("Returns 400 when name is missing")
        else:
            result.fail("Should return 400 when name is missing", 400, status)

    # Test: missing email
    response = add_student({"name": "Test User"})
    if response is not None:
        data, status = response
        if status == 400:
            result.ok("Returns 400 when email is missing")
        else:
            result.fail("Should return 400 when email is missing", 400, status)

    return result


def test_update_student():
    """Test the update_student function."""
    result = TestResult("update_student")
    reset_data()

    print("\nTesting update_student()...")

    # Test: update existing student
    response = update_student(1, {"major": "Machine Learning"})

    if response is None:
        result.fail("Function returns None - not implemented yet")
        return result

    if not isinstance(response, tuple) or len(response) != 2:
        result.fail("Should return (data, status_code) tuple")
        return result
    result.ok("Returns (data, status_code) tuple")

    student, status = response

    if status == 200:
        result.ok("Returns 200 for updated student")
    else:
        result.fail("Should return 200 for updated student", 200, status)

    if isinstance(student, dict) and student.get("major") == "Machine Learning":
        result.ok("Student major was updated")
    else:
        result.fail("Student major should be updated", "Machine Learning", student.get("major") if isinstance(student, dict) else None)

    # Test: original fields preserved
    if isinstance(student, dict) and student.get("name") == "Alice Smith":
        result.ok("Original name preserved")
    else:
        result.fail("Original name should be preserved")

    # Test: update non-existent student
    response = update_student(999, {"major": "Test"})
    if response is not None:
        data, status = response
        if status == 404:
            result.ok("Returns 404 for non-existent student")
        else:
            result.fail("Should return 404 for non-existent student", 404, status)

    return result


def test_delete_student():
    """Test the delete_student function."""
    result = TestResult("delete_student")
    reset_data()

    print("\nTesting delete_student()...")

    # Test: delete existing student
    response = delete_student(2)

    if response is None:
        result.fail("Function returns None - not implemented yet")
        return result

    if not isinstance(response, tuple) or len(response) != 2:
        result.fail("Should return (data, status_code) tuple")
        return result
    result.ok("Returns (data, status_code) tuple")

    data, status = response

    if status == 200:
        result.ok("Returns 200 for deleted student")
    else:
        result.fail("Should return 200 for deleted student", 200, status)

    # Test: student is actually removed
    check = get_student(2)
    if check is not None:
        _, check_status = check
        if check_status == 404:
            result.ok("Student was actually removed from data")
        else:
            result.fail("Student should be removed from data")

    # Test: delete non-existent student
    reset_data()  # Reset to test 404
    response = delete_student(999)
    if response is not None:
        data, status = response
        if status == 404:
            result.ok("Returns 404 for non-existent student")
        else:
            result.fail("Should return 404 for non-existent student", 404, status)

    return result


def main():
    """Run all tests and display summary."""
    print("=" * 60)
    print("Student Records API - Test Suite")
    print("=" * 60)

    results = [
        test_list_students(),
        test_get_student(),
        test_add_student(),
        test_update_student(),
        test_delete_student(),
    ]

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    total_passed = 0
    total_failed = 0

    for r in results:
        status = "PASS" if r.failed == 0 else "FAIL"
        print(f"  {r.name}: {r.passed} passed, {r.failed} failed [{status}]")
        total_passed += r.passed
        total_failed += r.failed

    print("-" * 60)
    print(f"  TOTAL: {total_passed} passed, {total_failed} failed")

    if total_failed == 0:
        print("\n  All tests passed! Great job!")
    elif total_passed == 0:
        print("\n  No tests passed yet. Keep working on it!")
    else:
        print(f"\n  Good progress! {total_passed}/{total_passed + total_failed} tests passing.")

    print("=" * 60)

    return 0 if total_failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
