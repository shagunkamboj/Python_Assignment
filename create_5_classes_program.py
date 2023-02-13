class Room:
    length = int(input("enter the length of the room ="))
    breadth = int(input("enter the breadth of the room = "))
    def Area1(self):
        print("the area of the room =",self.length*self.breadth)
class Bank_Account:
    balance = 109000
    Account_Number = 89034645547383
    def display2(self):
        print("the bank balance =",self.balance)
        print("the Account_Number =",self.Account_Number)
class Student:
    name = input("enter the name of the student = ")
    roll_no = int(input("enter the roll_no of the student ="))
    def display3(self):
        print("the name of the student=",self.name)
        print("the roll_no of the student =",self.roll_no)
class Employee:
    name = input("enter the name of the employee = ")
    Id = int(input("enter the Id of the student ="))
    def display4(self):
        print("the name of the employee =",self.name)
        print(" the id of the employee =",self.Id)
class Dog:
    legs = 4 
    eyes = 2 
    def display1(self):
        print("the legs of the dog =",self.legs)
        print("the eyes of the dog =",self.eyes)

obj5 = Room()
obj5.Area1()  


obj2 = Bank_Account()
obj2.display2()

obj3 = Student()
obj3.display3()

obj4 = Employee()
obj4.display4()

obj1 = Dog()
obj1.display1()
