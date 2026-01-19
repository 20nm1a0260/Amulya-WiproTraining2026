# #& Functions in Python 

# # Defining a function

# def add(a,b): 
#     return a+b 

# print(add(1,23))  

# def add(d,e):
#     print(d+e)

# add(21.32,32)


# def hello(name):
#     return f"greetings {name}"

# print(hello("sai prakash"))


# #$args parameters - arguments

# def print_args(*args):
#     print(args)

# print("hi")
# print("saiprakash")
# print(32)

# #$*Kwargs - keyword args

# def print_param1(**kwargs):
#     print(kwargs)

# print_param1(x=1,y=232,z="saiprakash")
    

# #! Module

# import math as m

# from math import sqrt,cos,sin

# print(sqrt(9))
# print(sin(180))
# print(cos(0))


#! OOPS object oriented programing

#& creating class without the constructor

# class Student: #class creation  
#     name="saiprakash"
#     age=22

# s1=Student()  #object creation
# print(f"my name is {s1.name} and my age is  {s1.age}")


#& creating class with the help of constructor

# class Employee:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# e1=Employee("sai",23)
# e2=Employee("prakash",24)
# print(e1.name)
# print(e1.age)
# print(e1.name+e2.name)
# print(e1.age+e2.age)
# #print(e1+e2) #error


#! Iterator

# data=[1,2,3,4,5]
# it=iter(data)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

#& for loop has builtin iterator.

# data=[1,2,3,4,5,6]
# for x in data:
#     print(x,end="")


#& custom iterator

# class Count:
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
# obj=Count(3)

# for num in obj:
#     print(num)

        
#! Generator -- using yield keyword

# simple way of creating an iterator using yield keyword.

# def numbers():
#     yield 1
#     yield 2
#     yield 3

# gen=numbers()
# print(next(gen))
# print(next(gen))
# print(next(gen))


#* example

# def count_up(n):
#     for i in range(1,n+1):
#         yield i 

# for val in count_up(10):
#     print(val,end="")



#! File handling

#* this is reading and printing in terminal

# file=open("Python Selenium Notes/file.txt","r")
# content=file.readline()
# content1=file.readlines()

# print(content)
# print(content1)

# file.close()

#* this is appending the txt into text file

# file=open("Python Selenium Notes/file.txt","a")

# file.write("\n New line added")

# file.close()

#* this is writing into the file-- this deletes the previos data and writes new


# file=open("Python Selenium Notes/file.txt","w")

# file.write("Hi this is write mode" )
# file.write("Hi this is write mode second time" )

# file.close()


#! file handling in json file

# import json

# data={
#     "name":"saiprakashreddy",
#     "age":25,
#     "skills":["python","selenium"],
#     "place":"Hyderabad"
# }

# with open("Python_Selenium_Notes/data.json","w") as file:
#     json.dump(data,file,indent=18)


#file handling in csv

# import csv

# with open("Python_Selenium_Notes/student.csv","w",newline="") as file:
#     writer=csv.writer(file)
#     writer.writerow(["Name","Id","Age"])
#     writer.writerow(["saiprakash",1,22])
#     writer.writerow(["prakash",2,82])


#! file handling in xml file

#& reading from xml file

# import xml.etree.ElementTree as ET
# tree=ET.parse("Python_Selenium_Notes/student.xml")
# root=tree.getroot()

# for student in root.findall("student"):
#     id=student.find("id").text 
#     name=student.find("name").text 
#     marks=student.find("marks").text 
#     print(id,name,marks)


#& writing into xml file

# root=ET.Element("employee")

# emp1=ET.SubElement(root,"emp")
# ET.SubElement(emp1,"id").text="1"
# ET.SubElement(emp1,"Name").text="Sai"
# ET.SubElement(emp1,"Salary").text="10000"

# emp1=ET.SubElement(root,"emp")
# ET.SubElement(emp1,"id").text="2"
# ET.SubElement(emp1,"Name").text="Prakash"
# ET.SubElement(emp1,"Salary").text="20000"

# tree=ET.ElementTree(root)
# tree.write("Python_Selenium_Notes\employee.xml")
# print("Xml file written successfully")


#! decorator -- changes the functionality of the code ,without changing the actual code

# def mydecorator(func):
#     def wrapper():
#         print("Before Function call")
#         func()
#         print("After Function call")
#     return wrapper

# @mydecorator
# def sayhello():
#     print("Hello")

# sayhello()


#! Descriptor -- used to manage the attributes of different classes

# class mydescriptor:
#     def __get__(self,obj,owner):
#         print("Getting value")
#         return obj._x
#     def __set__(self,obj,value):
#         print("Setting the value")
#         obj._x=value

# class Test:
#     x=mydescriptor

# t=Test()
# t.x=10
# print(t.x)  

#! Enum - assigning the fixed values or restricting the other values

#* example 1
from enum import Enum

# class color(Enum):
#     Red=1
#     Green=2
#     Blue=3

# print(color.Red.value)
# print(color.Green.value)


#* example 2

class gender(Enum):
    Male="M"
    Female="F"
print("Name","Sai prakash")
print("Gender:",gender.Male.value)