
#! OOPs

#& classes and objects

#* example 1

# class Student:
#     def display(self):
#         print("This is student class")

# s1=Student()
# s1.display()


#* example 2

# class Calculator:
#     def add(self,a,b):
#         print("sum :",a+b) 

# c1=Calculator()
# c1.add(332,32)



#! constructors and destructors.

# class Employee:
#     def __init__(self,name): #constructor
#         self.name=name 
#         print("constructor is called")

#     def __del__(self): #destructor
#         print("Destructor is called")

# e1=Employee("sai")



#! abstraction

# from abc import ABC, abstractmethod

# class shape(ABC):

#     def display(self):
#         print("normal method")

#     @abstractmethod
#     def area(self):
#         pass

# class reactangle(shape):
#     def area(self):
#         print("area method implemented")

# r=reactangle()
# r.area()
# r.display()



#! constructor with abstract class


# from abc import ABC,abstractmethod

# class Employee(ABC):
#     def __init__(self,name):
#         self.name=name

#     @abstractmethod
#     def salary(self):
#         pass


# class Manager(Employee):
#     def salary(self):
#         print(self.name,"Your salary is 50000")

# m=Manager("Sai")
# m.salary()


#! Multiple Abstract methods- more than 1 abstract methods


from abc import ABC,abstractmethod

class Bank(ABC):

    @abstractmethod
    def interest(self):
        pass

    @abstractmethod
    def loan(self):
        pass

class Sbi(Bank):

    def interest(self):
        print("Interest is 6% pa")

    def loan(self):
        print("loan amount is 40000")

s=Sbi()
s.loan()
s.interest()
