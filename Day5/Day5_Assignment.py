
#! Question – Class Types & Inheritance

#~ Topics: Class types, Introduction to Inheritance, Types of Inheritance

#* Question 1

'''1. Create a base class Vehicle with a method start()			
			
2. Create a derived class Car that inherits from Vehicle			
			
3. Add a class variable to track the number of vehicles created			
			
4. Demonstrate single inheritance and multilevel inheritance with appropriate classes			
'''

# class Vehicle:
#     Vehicle_count=0
    
#     def __init__(self):
#         Vehicle.Vehicle_count+=1 
        
#     def start(self):
#         print("Vehicle started")
        
#* single Inheritance

# class Car(Vehicle):
#     def drive(self):
#         print("car is driving")
        
#* Multi level inheritance

# class Evcar(Car):
#     def charge(self):
#         print("Electric car is charging")
        
# v=Vehicle()
# c=Car()
# e=Evcar()

# v.start()
# c.start()
# c.drive()

# e.start()
# e.drive()
# e.charge()

#! Question – Polymorphism (Method & Operator Overloading)

#~ Topics: Introduction to Polymorphism, Polymorphism on Operators

'''
    1. Create a class Calculator that demonstrates method overriding			
				
	2. Create another class AdvancedCalculator that overrides a method from Calculator			
				
	3. Implement operator overloading by overloading the + operator to add two objects of a custom class			
				
	4. Demonstrate polymorphism using the same method name with different behaviors			
 		
'''

class Calculator:
    def calculate(self, a, b):
        print("Calculator: Performing addition")
        return a + b


class AdvancedCalculator(Calculator):
    def calculate(self, a, b):
        print("AdvancedCalculator: Performing multiplication")
        return a * b


class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __str__(self):
        return str(self.value)

def show_result(calculator, a, b):

    result = calculator.calculate(a, b)
    print("Result:", result)


calc = Calculator()
adv_calc = AdvancedCalculator()

show_result(calc, 10, 5)       
show_result(adv_calc, 10, 5)  

n1 = Number(20)
n2 = Number(30)

n3 = n1 + n2  
print("Sum using overloaded + :", n3)
