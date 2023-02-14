class Room:
    def __init__(self,length,breadth):
        self.length = length 
        self.breadth = breadth 
    def Area(self):
        print("the area of the room =",self.length * self.breadth)
class Bank_Account:
    def __init__(self,balance,Account_Number):
        self.balance = balance 
        self.Account_Number = Account_Number
    def display2(self):
        print("the bank balance =",self.balance)
        print("the Account_Number =",self.Account_Number)
class Student:
    def __init__(self,name,roll_no):
        self.name = name 
        self.roll_no = roll_no
    def display3(self):
        print("the name of the student=",self.name)
        print("the roll_no of the student =",self.roll_no)
class Employee:
    def __init__(self,name,Id):
        self.name = name 
        self.Id = Id
    def display4(self):
        print("the name of the employee =",self.name)
        print(" the id of the employee =",self.Id)
class Dog:
    def __init__(self,legs,eyes):
        self.legs = legs 
        self.eyes = eyes 
    def display5(self):
        print("the legs of the dog =",self.legs)
        print("the eyes of the dog =",self.eyes)
obj1 = Room(3,5)
obj1.Area()  


obj2 = Bank_Account(100000,78907564444)
obj2.display2()

obj3 = Student('shagun',6)
obj3.display3()

obj4 = Employee('A',90)
obj4.display4()

obj5 = Dog(4,2)
obj5.display5()