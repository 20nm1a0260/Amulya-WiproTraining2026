
# # first program

# print("Hello world")


# # eligible to vote or not

# x=int(input("Enter your age:"))

# if x>=18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")
 
 
#  arithmetic operators
 
# a=10
# b=23
# print("Addition",a+b)
# print("Subtraction",a-b)
# print("Multiplication",a*b)
# print("Division",a/b)
# print("Modulus",a%b)
# print("Floor division",a//b)

#math function

# import math

# print(math.sqrt(8))
# print(math.log(100))
# print(math.gamma(100))

#Boolean 

# a=20
# b=300
# if(a==b):
#     print("Equal")
# else:
#     print("Not Equal")   
    
#Strings

#these are immutable


# a="Hello"

# #indexing

# print(a[0])
# print(a[-1])
# print(a)

# #slicing

# text="saiprakashreddy"
# print(text[0:2])
# print(text[::-1])

# #concat

# print(text+a)

# #repetation

# print(text*3)

# print(text.upper())
# print(text.lower())
# print(text.replace("sai","java"))
# print(text.isalpha())
# print(text.isdigit())
# print(len(text))
# print(text.find("a"))
# print("a" in "apple")
# print("a" not in "apple")

# s1="I am {0} and I'm {1} years old".format("sai",23)
# print(s1)

# s2=text.split()
# print(s2)

#-------------data types-----------------

#list is mutable----------------

# numbers=[1,2,3,4,5]
# names=["sai","prakash","reddy"]
# mixed=[1,"sai",0.232,True]

# # we can do both slicing and indexing
# print(numbers[1])
# print(names[::-1])
# print(mixed[:2])

# numbers[1]=100
# print(numbers)

# #printing all the values in list

# for i in numbers:
#     print(i)


# print(10 in numbers)


# #adding

# matrix=[[1,2,3],[4,5,6]]
# print(matrix)
       

#  #reversing the list

# hi=[1,2,3,4,5,6,7,8,9,10]

# hi.reverse()
# print(hi)

# #adding the values in list

# hi.append("sai")
# print(hi)

# hi.extend(matrix)
# print(hi)

# hi.insert(0,"prakashreddy")
# print(hi)

# #removing from list

# hi.remove("sai")
# print(hi)

# hi.pop()
# print(hi)

# #sorting the list

# matrix.sort()
# print(matrix)

# matrix.sort(reverse=True)
# print(matrix)


#Tuple-------- 

#this is immutable

# hi=(1,2,3,4,5,6,2)
# print(hi)

# #indexing and slicing

# print(hi[1])
# print(hi[::-1])

# #we can't add into tuple

# print(hi.count(2))
# print(hi.index(1))

# #Swapping the values

# a=5
# b=10
# a,b=b,a
# print(a,b)

# data=10,20,30 #packing
# a,b,c=data #unpacking
# print(a,b,c)


#dictionary --------- mutable

# student={
#     "name":"saiprakash",
#     "age":22,
#     "place":"hyd",
# }

# print(student)

# #accessing the content of dict

# print(student)
# print(student["name"])
# print(student.get("age"))

# #adding  and changing in dict

# student["marks"]=55
# student["age"]=32
# print(student)

# #removing the elements in dict

# student.pop("age")
# student.popitem() #it pops the last item
# print(student)

# #displaying the keys 

# print(student.keys())

# #displaying the values

# print(student.values())

# #displaying the items

# print(student.items())

#iterating over the dict

# for key in student:
#     print(key,student[key])

#checking whether key is present or not

# if "name" in student:
#     print('key exists')
# else:
#     print("key not exists")    

 #nested dict

# employees={
#     101:{"name":"Sai","salary":23433},
#     102:{"name":"prakash","salary":32322}
# }

# print(employees)
# print(employees[102])
# print(employees[102]["salary"])


##Set ------- unique and muttable

# sai={1,2,3,4,34,3,3,5}

# print(sai)

# #accessing the elements of set

# for i in sai:
#     print(i)


# #adding

# sai.add(100)
# print(sai)

# #operations on set

# A={1,2,3}
# B={3,4,5}
# print(A| B) #union
# print(A&B) #intersection
# print(2 in A) #checking or membership operator


#control structures in Python

#if else statement


# num=5
# if num%2==0:
#     print("Even")
# else:
#     print("odd") 

#elif statement


# marks=80
# if marks>=90:
#     print("Grade A")
# elif marks>=80:
#     print("Grade B")
# else:
#     print("Grade C")


#for loop

# for i in range(1,6):
#     print(i)


#while loop

# j=1
# while j<=5:
#     print(j)
#     j+=1

# #match case

# day=1

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
    

#break, continue,pass


# for i in range(1,10):
#     if i==2:
#         continue
#     if i==3:
#         pass #just for time pass 
#     if i==5:
#         break   
#     print(i)


# lambda function --- small function without name


#lambda args:exps  --- syntax


# add=lambda x:x+3
# print(add(7))

# subtract=lambda a,b : a-b 
# print(subtract(42,23))

# multi=lambda c,d:c*d
# print(multi(2,5))

# maxnum=lambda x,y:x if x>y else y
# print(maxnum(100,22))



#map(function,iterable)--- syntax

# numbers=[1,2,3,4,5]
# result=map(lambda x:x*2,numbers)
# print(list(result))


