# Import SQLite and Connect to Database

import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("company.db")

# Create a cursor object
cursor = connection.cursor()

# Find Employee(s) with the Highest Salary Overall
query1 = """
SELECT employee_name, department, salary
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
);
"""

cursor.execute(query1)

print("Employee(s) with the Highest Salary:\n")

for row in cursor.fetchall():
    print(row)
    
# Find Department(s) with the Highest Average Salary
query2 = """
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING AVG(salary) = (
    SELECT MAX(avg_salary)
    FROM (
        SELECT AVG(salary) AS avg_salary
        FROM employees
        GROUP BY department
    )
);
"""

cursor.execute(query2)

print("\nDepartment(s) with the Highest Average Salary:\n")

for row in cursor.fetchall():
    print(row)
    
# Find Employees Earning More Than the Average Salary in Their Department
query3 = """
SELECT employee_name, department, salary
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
    WHERE department = e.department
);
"""

cursor.execute(query3)

print("\nEmployees Earning More Than Their Department Average:\n")

for row in cursor.fetchall():
    print(row)
    
# Close the Database Connection
cursor.close()
connection.close()