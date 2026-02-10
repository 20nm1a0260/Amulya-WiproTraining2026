
# ✅ What is Pandas?

# Pandas is a Python library built on top of NumPy.
# It is used for data analysis and data manipulation.
# It works mainly with structured data (like tables).


# ✅ Core Data Structures in Pandas

# 1. Series  → One-dimensional data (like a single column).
# 2. DataFrame → Two-dimensional table (rows and columns).


# ✅ Common Operations in Pandas

# 1. Creating a DataFrame.
# 2. Filtering rows.
# 3. Adding new columns.
# 4. Grouping data.
# 5. Handling missing values.


# ✅ Example

import pandas as pd  # Importing Pandas library

# Creating structured data (list of dictionaries)
data = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92}
]

# Creating a DataFrame from the data
df = pd.DataFrame(data)

# Adding a new column "passed"
# This checks if score is greater than 80 (True/False)
df["passed"] = df["score"] > 80

# Printing the DataFrame
print(df)
