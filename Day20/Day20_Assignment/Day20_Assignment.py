#& =========================================================
#& 1️⃣ NUMPY / PANDAS – DATA MANIPULATION
#& =========================================================

#~ Given:
# students = [
#     {"name": "Alice", "score": 85},
#     {"name": "Bob", "score": 92},
#     {"name": "Charlie", "score": 78},
#     {"name": "David", "score": 90},
#     {"name": "Eva", "score": 88}
# ]

#todo Step 1:
# Convert the list of dictionaries into a Pandas DataFrame

#todo Step 2:
# Extract the "score" column as a NumPy array

#todo Step 3:
# Using NumPy, calculate:
#* Mean of scores
#* Median of scores
#* Standard Deviation of scores

#todo Step 4:
# Create a new column "above_average"
# Condition:
# If student's score > mean → True
# Else → False

#! Ans : Refer Question1 folder 

#& =========================================================
#& 2️⃣ DATAFRAME OPERATIONS
#& =========================================================

#~ Given DataFrame:
# Employee   Department   Salary
# John                      IT              50000
# Alice                     HR              60000
# Bob                       IT                55000
# Eva                       Finance      65000
# Mark                     HR               62000


#todo Task 1:
# Filter all employees from "IT" department

#todo Task 2:
# Calculate average salary per department
# Hint:
# Group by Department
# Then calculate mean of Salary

#todo Task 3:
# Add new column "Salary_Adjusted"
# Increase each employee salary by 10%
# (Salary * 1.10)

#! Ans : Refer Question2 folder