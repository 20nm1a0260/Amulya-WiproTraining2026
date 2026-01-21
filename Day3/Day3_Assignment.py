
#! Question – Decorators

#& 1)Write a decorator called @execution_time that:

#*1. Measures the execution time of a function

#*2. Prints the function name and execution time

import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f} seconds")
        return result
    return wrapper


@execution_time
def test():
    time.sleep(2)

test()


#! Question – Functions, Modules, File Handling & Exceptions

#&Create a small Python package with:

#* 1. A module containing a function write_numbers_to_file(filename)

# def write_numbers_to_file(filename):
#     with open(filename, "w") as file:
#         for i in range(1, 11):
#             file.write(str(i) + "\n")

# write_numbers_to_file("Assignment/file1.txt")
# print("File created successfully")

#* 2. The function should write numbers 1–100 into a file

# def write_numbers_to_file(filename):
#     with open(filename, "w") as file:
#         for i in range(1, 101):
#             file.write(str(i) + "\n")

# write_numbers_to_file("Assignment/file2.txt")
# print("File created successfully")

#* 3. Handle possible exceptions such as:

#* File not found

#* Permission denied

# def write_numbers_to_file(filename):
#     try:
#         with open(filename, "w") as file:
#             for i in range(1, 11):
#                 file.write(str(i) + "\n")

#         print("Numbers written successfully")

#     except FileNotFoundError:
#         print("Error: File path not found")

#     except PermissionError:
#         print("Error: Permission denied to write the file")

#     except Exception as e:
#         print(f"Unexpected error: {e}")

# write_numbers_to_file("Assignment/file3.txt")
# write_numbers_to_file("invalid_folder/numbers.txt")
# write_numbers_to_file("C:/Windows/System32/numbers.txt")

#* 4. Create another module that imports this function and reads the file content safely

# def read_file_safely(filename):
#     try:
#         with open(filename, "r") as file:
#             content = file.read()
#             return content

#     except FileNotFoundError:
#         return "Error: File not found"

#     except PermissionError:
#         return "Error: Permission denied"

#     except Exception as e:
#         return f"Unexpected error: {e}"

# print(read_file_safely("Assignment/file3.txt"))
