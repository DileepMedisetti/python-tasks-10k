# ==========================================
# Assignment: PDBC CRUD Operations
# ==========================================

import mysql.connector

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",      # Change if needed
    database="company_db"
)

cursor = connection.cursor()

# -------------------------------
# Login
# -------------------------------

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "admin" and password == "admin123":

    print("\nLogin Successful!")
    print("Welcome", username)

    while True:

        print("\n===== MENU =====")
        print("1. Insert Employee")
        print("2. Display Employees")
        print("3. Update Salary")
        print("4. Delete Employee")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        # -------------------------------
        # Create
        # -------------------------------

        if choice == 1:

            emp_id = int(input("Enter Employee ID: "))
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            salary = int(input("Enter Salary: "))

            sql = "INSERT INTO employees VALUES(%s,%s,%s,%s)"
            values = (emp_id, name, dept, salary)

            cursor.execute(sql, values)
            connection.commit()

            print("Employee Added Successfully.")

        # -------------------------------
        # Read
        # -------------------------------

        elif choice == 2:

            cursor.execute("SELECT * FROM employees")

            records = cursor.fetchall()

            print("\nEmployee Details")

            for row in records:
                print(row)

        # -------------------------------
        # Update
        # -------------------------------

        elif choice == 3:

            emp_id = int(input("Enter Employee ID: "))
            salary = int(input("Enter New Salary: "))

            sql = "UPDATE employees SET salary=%s WHERE emp_id=%s"

            cursor.execute(sql, (salary, emp_id))
            connection.commit()

            print("Employee Updated Successfully.")

        # -------------------------------
        # Delete
        # -------------------------------

        elif choice == 4:

            emp_id = int(input("Enter Employee ID: "))

            sql = "DELETE FROM employees WHERE emp_id=%s"

            cursor.execute(sql, (emp_id,))
            connection.commit()

            print("Employee Deleted Successfully.")

        # -------------------------------
        # Exit
        # -------------------------------

        elif choice == 5:

            print("Thank You!")
            break

        else:
            print("Invalid Choice")

else:

    print("Invalid Username or Password")

cursor.close()
connection.close()