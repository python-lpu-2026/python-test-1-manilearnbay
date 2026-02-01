"""
Q3. JSON Data Pipeline with Functional Programming

You are given a JSON file containing employee data:
[
  {"name": "Amit", "department": "IT", "salary": 60000},
  {"name": "Riya", "department": "HR", "salary": 45000},
  {"name": "John", "department": "IT", "salary": 80000}
]


Write a function:
def high_earners_by_department(filename, department, min_salary):

Requirements:
1. Load JSON safely
2. Filter employees:
    a. matching department
    b. salary ≥ min_salary
3. Use:
    a. filter
    b. lambda
4. Return a list of names sorted by salary (descending)

Error handling
Invalid json file => return empty list []
"""

import json
def high_earners_by_department(filename, department, min_salary):
    try:
        with open(filename) as f:
            data = json.load(f)

        filtered = filter(
            lambda e: e.get("department") == department and e.get("salary", 0) >= min_salary,
            data
        )

        return [
            e["name"]
            for e in sorted(filtered, key=lambda x: x["salary"], reverse=True)
        ]
    except Exception:
        return []

