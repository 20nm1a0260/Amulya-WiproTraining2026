#! Question – Introduction to OOPs, Classes & Objects

#& Create a class Student that:	

''' 
1. Has attributes name and roll_no	
	
2. Has a method display_details() to print student information	
	
3. Create at least two objects of the class and display their details	
'''

class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    
    def display_details(self):
        print(" Name:",self.name," Rollno: ",self.roll_no)

s1=Student("Saiprakash",12)
s2=Student("Ram",34)

s1.display_details()
s2.display_details()

#! Question – Parameterized Methods, Constructors & Destructors

'''
Create a class BankAccount that:		
		
1. Uses a parameterized constructor to initialize account_number and balance		
		
2. Implements methods deposit(amount) and withdraw(amount)		
		
3. Uses a destructor to display a message when the object is deleted		
		
4. Handle invalid withdrawal using proper checks		

'''

class BankAccount:

    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance

    def deposit(self,amount):
        self.amount=amount
        self.balance=self.amount+self.balance
        print(self.amount ,"RS deposited successfully")
        print("Total balance is :",self.balance,"RS")

    def withdrawn(self,amount):
        self.amount=amount
        if self.balance>=self.amount:
            self.balance=self.balance-self.amount
            print(self.amount,"RS withdrawn successfully")
            print("Total balance is :",self.balance,"RS")
        else:
            print("oops sorry!! Insuffient funds")

b=BankAccount(123,1000)
b.deposit(1000000000)
b.withdrawn(20000)