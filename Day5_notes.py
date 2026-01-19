#! Inheritance in python

# class Animal:
#     def speak(self):
#         print("Animal makes a sound")
        

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")
        
# d=Dog()
# d.speak()
# d.bark()

#~ Mutiple Inheritance

# class A:
#     def showA(self):
#         print("A")
    
# class B:
#     def showB(self):
#         print("B")
        
# class C(A,B):
#     pass 

# c=C()
# c.showA()
# c.showB()


#! Multi level inheritance

# class A:
#     def a(self):
#         print("A")
    
# class B(A):
#     def b(self):
#         print("B")
        
# class C(B):
#     def c(self):
#         print("C")
    
# obj=C()
# obj.c()
# obj.b()
# obj.a()

#! Hierarchical Inheritance

# class Parent:
#     def parent1(self):
#         print("Parent1")
        
# class Child1(Parent):
#     def c1(self):
#         print("child1")

# class Child2(Parent):
#     def c2(self):
#         print("child2")
        
# obj1=Child1()
# obj1.c1() 
# obj1.parent1()

# obj2=Child2()
# obj2.c2()
# obj2.parent1()

#! polymorphism

#& operator overloading

# class Box:
#     def __init__(self,value):
#         self.value=value  
        
#     def __add__(self,other): #dunder function
#         return self.value+other.value
    
# b1=Box(50)
# b2=Box(30)

# b3=(b1+b2)
# print(b3)


#! method overriding

# class animal:
#     def sound(self):
#         print("animal sound")
        
# class dog(animal):
#     def sound(self):
#         print("dog barks")
        
# class cat(animal):
#     def sound(self):
#         print("Cat meows")
        

# obj=[dog(),cat()]
# for a in obj:
#     a.sound()