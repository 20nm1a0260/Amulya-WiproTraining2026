
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="root", database="wipro_database"
)

# Fetch all employees whose salary >5000
cursor = conn.cursor()
cursor.execute("SELECT * FROM employee WHERE Employee_Salary > 50000")
employees = cursor.fetchall()

print("Employees with salary>50000:")
for emp in employees:
    print(emp)


# insert a new employee

insert_query = """
INSERT INTO employee (Employee_id, Employee_Name,Employee_Salary)
VALUES (%s,%s,%s)"""

values = (108, "riya", 38000)

cursor.execute(insert_query, values)

conn.commit()
print("\n New employee inserted successfully.")

# Increase salary by 10%  for a specific employee

update_query = """
UPDATE employee
SET Employee_Salary = Employee_Salary *1.10
WHERE Employee_Name =%s """

cursor.execute(update_query, ("Sai",))
conn.commit()
print("Salary updated successfully.")

# Display final table

print("\n Final Employee table:")
cursor.execute("SELECT * from employee")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
