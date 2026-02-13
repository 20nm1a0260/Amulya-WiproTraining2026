
# ============================================================
# 1️⃣ THREADING (I/O-BOUND TASK)
# ============================================================

# Problem:
# You need to download data from multiple URLs at the same time.

# Given:
# urls = [
#     "https://example.com/data1",
#     "https://example.com/data2",
#     "https://example.com/data3",
#     "https://example.com/data4"
# ]

# Task:
# 1. Use threading to download all URLs concurrently.
# 2. Save each URL’s content into separate text files:
#    data1.txt, data2.txt, data3.txt, data4.txt.
# 3. Measure and print:
#       - Time taken for sequential downloads
#       - Time taken for threaded downloads
#
# Hint:
# - Use requests library to download data.
# - Use threading.Thread for concurrency.
# - Use time module to measure execution time.

# & Ans : refer Question 1 folder

# ============================================================
# 2️⃣ MULTIPROCESSING (CPU-BOUND TASK)
# ============================================================

# Problem:
# You need to calculate factorials of very large numbers.
# This is a CPU-intensive task.

# Given:
# numbers = [50000, 60000, 55000, 45000, 70000]

# Task:
# 1. Use multiprocessing to calculate factorial of each number in parallel.
# 2. Print the factorial of each number.
# 3. Measure and compare:
#       - Time taken using sequential computation
#       - Time taken using multiprocessing
#
# Hint:
# - Use math.factorial() function.
# - Use multiprocessing.Pool or Process.
# - Use time module to measure execution time.

# & Ans : refer Question 2 folder
