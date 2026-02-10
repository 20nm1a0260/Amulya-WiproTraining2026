
# ✅ What is NumPy?

# NumPy is a Python library used for numerical computing.
# It works with arrays (called ndarray).
# It is faster than Python lists for mathematical operations.
# It is widely used in Data Science, Machine Learning, and AI.


# ✅ Key Features of NumPy

# 1. Supports multi-dimensional arrays.
# 2. Provides mathematical operations.
# 3. Includes statistical functions.
# 4. Offers linear algebra support.
# 5. Supports broadcasting (operations on arrays of different shapes).


# ✅ Example

import numpy as np  # Importing NumPy library

# Creating a NumPy array
arr = np.array([85, 92, 78, 90, 88])

# Calculating mean (average)
mean = np.mean(arr)

# Calculating median (middle value)
median = np.median(arr)

# Calculating standard deviation (spread of data)
std = np.std(arr)

# Printing the results
print(mean, median, std)
