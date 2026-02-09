#!/bin/bash
# Week 3 In-Class Exploration: Test Commands
# Run these to test your API implementation

echo "=== Testing Student Records API ==="
echo ""

echo "1. GET /students (list all)"
curl -s http://localhost:5000/students | python3 -m json.tool
echo ""

echo "2. GET /students/1 (get one - should succeed)"
curl -s http://localhost:5000/students/1 | python3 -m json.tool
echo ""

echo "3. GET /students/99 (get one - should 404)"
curl -s http://localhost:5000/students/99 | python3 -m json.tool
echo ""

echo "4. POST /students (create new)"
curl -s -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"name": "Dan Brown", "email": "dan@berkeley.edu", "major": "Statistics"}' \
  | python3 -m json.tool
echo ""

echo "5. POST /students (missing name - should 400)"
curl -s -X POST http://localhost:5000/students \
  -H "Content-Type: application/json" \
  -d '{"email": "noname@berkeley.edu"}' \
  | python3 -m json.tool
echo ""

echo "6. PUT /students/1 (update)"
curl -s -X PUT http://localhost:5000/students/1 \
  -H "Content-Type: application/json" \
  -d '{"major": "Machine Learning"}' \
  | python3 -m json.tool
echo ""

echo "7. DELETE /students/2"
curl -s -X DELETE http://localhost:5000/students/2 | python3 -m json.tool
echo ""

echo "8. GET /students (verify changes)"
curl -s http://localhost:5000/students | python3 -m json.tool
echo ""

echo "=== Done! ==="
