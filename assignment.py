# [
# {
#   'roll_num':1,
#   'name': John,
#   'subjects':[Hindi, English],
#   'class':'Five'
# }]

# 1. List Students
# 2. Search Student
# 3. Update Student
# 4. Delete Student
# 5. Add Student
# 6. Exit
# Please choose option:
# list1 = [{'roll_num':1,'name': ['john','a','b'],'subjects':['Hindi', 'English'],'class':'Five'}]
# option = int(input("enter the option !!"))
# if option == 1:
#     print("list of the students!!")
#     print(list1)
    
# elif option == 2:
#     m = input("search the student !!")
#     if m in list1:
#         print("the name is present")
#         print(list1)
#     else:
#         print("name is not present")
# elif option == 3:
#     print("update the student !!")
#     m1 = dict(input("enter the student that you want to update = "))
#     m2 = dict(input("enter the new updated name = "))
#     m1.update(m2)
#     print(m1)
    
# elif option == 4:
#     print("delete  student")
#     d = input("enter the student that you want to delete=")
#     d1 = list.search 
# elif option == 5:
#     print("add the student that you want to add =")
# else:
#     print("exist from the menu")
user = []
dict = {}
dict['subjects']=[]
def list_of_students(user):
    return user 
def update(user):
    id = int(input("enter the id you want to update ="))
    name = input("enter the name of the student you want to update =")
    subject = input("enter the subject you want to update =")
    clas = int(input("enter the class you want to update ="))
    for i in user:
        if i['rollno'] == id:
            dict['name'] = name 
            dict['subject'] = subject
            dict['clas'] = clas 
def search(user):
    name = input("enter the name you want =")
    for i in user:
        if i['name'] == name:
            user = i
        else:
            print("user is not present")
    return user
def add(user):
    id = int(input("enter the id you want ="))
    name = input("enter the name of the student=")
    subject = input("enter the subject you want =")
    clas = int(input("enter the class ou want="))
    dict['id'] = id
    dict['name']=name
    dict['subjects'].append(subject)
    dict['clas'] = clas
    user.append(dict)
    return dict
def delete (user):
    rollno = int(input("enter the rollno you want to delete"))
    for i in user:
        if i[rollno] == id:
            user.remove(i)
    
while True:
    print("1->for list of the student =")
    print("2->for update ")
    print("3-> for searching")
    print("4->for adding students")
    option = int(input("enter the option you want"))
    if option == 1:
        r = list_of_students(user)
        print("the list of the student =",r)
    elif option == 2:
        r = update("after updation=",user)
        print(r)
    elif option == 3:
        r = search("after seraching =",user)
        print(r)
    elif option == 4:
        r = add("after adding =",user)
        print(r)
    elif option == 5:
        r = delete("after deletion =",user)
        print(r)
    elif option == 6:
        print("enter the valid option")
        break
    else:
        print("exist")
        break
