import json
import csv
import time
from abc import ABC, abstractmethod


def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper

def admin_only(func):
    def wrapper(*args, **kwargs):
        if not kwargs.get("is_admin", False):
            print("Access Denied: Admin privileges required")
            return
        return func(*args, **kwargs)
    return wrapper

def performance_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] Execution Time: {end-start:.6f} seconds")
        return result
    return wrapper


class MarksDescriptor:
    def __get__(self, instance, owner):
        return instance._marks

    def __set__(self, instance, value):
        if not all(0 <= m <= 100 for m in value):
            raise ValueError("Marks should be between 0 and 100")
        instance._marks = value

class SalaryDescriptor:
    def __get__(self, instance, owner):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, instance, value):
        instance._salary = value


class Person(ABC):
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        print(f"Cleaning up {self.name} record")

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def get_details(self):
        print("Student Details:")
        print("--------------------------------")
        print(f"Name      : {Amulya}")
        print("Role      : Student")
        print(f"Department: {BTech}")

    @log_execution
    @performance_timer
    def calculate_performance(self):
        avg = sum(m for m in self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return avg, grade

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)


class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        print("Faculty Details:")
        print("--------------------------------")
        print(f"Name      : {Rani}")
        print("Role      : Faculty")
        print(f"Department: {BTech}")


class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits

class CourseIterator:
    def __init__(self, courses):
        self.courses = courses
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.courses):
            val = self.courses[self.index]
            self.index += 1
            return val
        raise StopIteration


def student_generator(students):
    print("Fetching Student Records...")
    for s in students:
        yield f"{s.pid} - {s.name}"

class FileManager:
    @staticmethod
    def save_json(students, filename="students.json"):
        data = []
        for s in students:
            data.append({
                "id": s.pid,
                "name": s.name,
                "department": s.department,
                "semester": s.semester,
                "marks": s.marks
            })
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        print("Student data successfully saved to students.json")

    @staticmethod
    def save_csv(students, filename="students_report.csv"):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
            for s in students:
                avg, grade = s.calculate_performance()
                writer.writerow([s.pid, s.name, s.department, round(avg,2), grade])
        print("CSV Report generated successfully")


students = []
faculty_list = []
courses = []

while True:
    print("\n1 Add Student\n2 Add Faculty\n3 Add Course\n4 Calculate Performance\n5 Compare Students\n6 Generate Reports\n7 Exit")
    choice = input("Enter choice: ")

    try:
        if choice == "1":
            sid = input("Student ID: ")
            if any(s.pid == sid for s in students):
                raise Exception("Student ID already exists")
            name = input("Name: ")
            dept = input("Department: ")
            sem = int(input("Semester: "))
            marks = list(map(int, input("Enter 5 marks: ").split()))
            s = Student(sid, name, dept, sem, marks)
            students.append(s)
            print("Student Created Successfully")

        elif choice == "2":
            fid = input("Faculty ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            salary = int(input("Salary: "))
            f = Faculty(fid, name, dept, salary)
            faculty_list.append(f)
            print("Faculty Created Successfully")

        elif choice == "3":
            code = input("Course Code: ")
            cname = input("Course Name: ")
            credits = int(input("Credits: "))
            fid = input("Faculty ID: ")
            fac = next(f for f in faculty_list if f.pid == fid)
            c = Course(code, cname, credits, fac)
            courses.append(c)
            print("Course Added Successfully")

        elif choice == "4":
            sid = input("Student ID: ")
            s = next(s for s in students if s.pid == sid)
            avg, grade = s.calculate_performance()
            print(f"Average: {avg:.2f}, Grade: {grade}")

        elif choice == "5":
            s1 = students[0]
            s2 = students[1]
            print(f"{s1.name} > {s2.name} :", s1 > s2)

        elif choice == "6":
            FileManager.save_json(students)
            FileManager.save_csv(students)

            print("Student Record Generator")
            for rec in student_generator(students):
                print(rec)

        elif choice == "7":
            print("Thank you for using Smart University Management System")
            break

    except Exception as e:
        print("Error:", e)