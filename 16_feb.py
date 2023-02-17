# print("----------------------------------------")
# class Parent:
#     def display_1(self):
#         print("this is the function inside the parent class")
# class Child(Parent):
#     def display_2(self):
#         print("this is the function inside the child class")
# obj1 = Child()
# obj1.display_1()
# obj1.display_2()
# #by using super keyward
# print("------------------single inheritance by using super keyward----------------------")
# class Employee:
#     def __init__(self,id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
# class Derived(Employee):
#     def __init__(self,id,name,salary,emails):
#         super().__init__(id,name,salary)
#         self.emails = emails
# emp_1 = Derived(101,"x",10000,"s@gmail.com")
# print(emp_1.id)
# print(emp_1.name)
# print(emp_1.salary)
# print(emp_1.emails)
# #multiple inheritance
# print("------------------------#multiple inheritance---------------------------")
# class Father:
#     def __init__(self):
#         self.name = "x"
#         self.age = 40
#     def display(self):
#         print("father's name = ",self.name)
#         print("father's age = ",self.age)
# class Mother:
#     def __init__(self):
#         self.name = "y"
#         self.age = 35
#     def display(self):
#         print("mother's name = ",self.name)
#         print("mother's age = ",self.age)
# #class Child(Father,Mother):
#     #pass
# class Child(Mother,Father):
#     pass
# obj = Child()
# obj.display()
# print("------------------------# MULTILEVEL-----------------------------------")

# class Grandparent:
#     def display_1(self):
#         print("this is parent grandparent class")
# class Father(Grandparent):
#     def display_2(self):
#         print("this is child class derived from the grandparent class")
# class Son(Father):
#     def display_3(self):
#         print("this is the son class derived from the father class")
# obj = Son()
# obj.display_1()
# obj.display_2()
# obj.display_3()
# #HIErarchical inheritance
# print("---------------------HIErarchical inheritance------------------------------")
# class Parent:
#     def func_1(self):
#         print("this is the parent class function")
# class Child1(Parent):
#     def func_2(self):
#         print("this is the child1 function")
# class Child2(Parent):
#     def func_3(self):
#         print("this is the child2 function")
# obj1 = Child1()
# obj1.func_1()
# obj1.func_2()



#*******************DUNDER METHOD IMPLEMENTATION 
class String:
    def __init__(self,string1):
        self.string1 = string1 
    def display(self):
        return self.string1
    def __add__(self,other): # add dunder method
        return self.string1 + other 
    def __len__(self): # length dunder method
        return len(self.string1)
obj = String("hiii")
print(obj + " " + "hello")
print(len(obj))

class Operator:
    def __init__(self,Marks):
        self.Marks = Marks 
    def __lt__(self,marks):
        return self.Marks<marks.Marks
obj1 = Operator(40)
obj2 = Operator(50)
obj3 = Operator(900)
obj4 = Operator(20)
print(obj1<obj2)
print(obj3<obj4)

