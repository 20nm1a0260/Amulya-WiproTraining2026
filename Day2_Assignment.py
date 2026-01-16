#!Question – Iterators and Generators

#& 1. Create a custom iterator class that iterates over numbers from 1 to N

# class Number:
#     def __init__(self,limit):
#         self.limit=limit
#         self.current=1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current<=self.limit:
#             val=self.current
#             self.current+=1
#             return val
#         else:
#             raise StopIteration
        
# obj=Number(int(input("Enter any number:")))
# for i in obj:
#     print(i)

#& 2. Create a generator function that yields the first N Fibonacci numbers.

# def fibonacci_num(n):
#     a, b = 0, 1
#     count = 0

#     while count < n:
#         yield a
#         a, b = b, a + b
#         count += 1

# obj=fibonacci_num(5)
# for i in obj:
#     print(i,end=" ")

#& 3. Demonstrate the difference between using the iterator and generator by printing values using a for loop

#! iterator example

# class FibonacciIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.a = 0
#         self.b = 1
#         self.count = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.count < self.limit:
#             val = self.a
#             self.a, self.b = self.b, self.a + self.b
#             self.count += 1
#             return val
#         else:
#             raise StopIteration

# obj=FibonacciIterator(5)
# for i in obj:
#     print(i,end=" ")


#generator example
# def fibonacci_generator(n):
#     a, b = 0, 1
#     count = 0

#     while count < n:
#         yield a
#         a, b = b, a + b
#         count += 1

# for i in fibonacci_generator(10):
#     print(i,end=" ")

#!  Question – Descriptors


#&Create a class Employee with attributes:name,salary

#&Implement a descriptor that:

#*1. Ensures salary is always a positive number

#*2. Raises a ValueError if a negative salary is assigned

#*3. Demonstrates the descriptor by creating multiple Employee objects


class Salary:
    def __get__(self, obj,objtype=None):
        return obj._salary

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        obj._salary = value

class Employee:
    salary = Salary()  

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  


emp1 = Employee("Sai", 30000)
emp2 = Employee("Ram", 45000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)

# Trying to assign a negative salary
try:
    emp3 = Employee("Krishna", -20000)
except ValueError as e:
    print("Error:", e)