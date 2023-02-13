import datetime
import re

def Registration_form(first_name,last_name,birthdate):
    return first_name
    return last_name
    return birthdate.strftime('%d/%m/%Y')
def email_address(email_enter):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat,email_enter):
        return email_enter
    else:
        return "please!! enter valid email_id"
def password_checker(password):
    flag = 0
    while True:
        if len(password)<=8:
            flag = -1
            print("enter the password having minimum length 8")
            break
        elif not re.search("[a-z]",password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]" , password):
            flag = -1
            break
        else:
            flag = 0
            return "Valid Password"
            pwd = maskpass.askpass(mask = "*")
            return pwd
            break
    if flag == -1:
        return "not a valid password"
# def login_details(email_id,password):
#     pass
# def after_login_successfully():
#     print("after login successfully")
# def update_details():
#     first_name = input("enter the name that you want to update")

while True:
    print("1. Register yourself first!!!!")
    print("2. login yourself!!! ")
    print("3. Exit")
    option = int(input("Please Choose One Options:"))
    if option  == 1:
        first_name = input("enter the first name =")
        last_name = input("enter the last name =")
        birthday = input('Enter your birthday in dd/mm/yyyy format')
        day, month, year = list(map(int, birthday.split("/")))
        birthdate = datetime.date(year,month,day)
        a = Registration_form(first_name,last_name,birthday)
        print("first_name = ",first_name)
        print("last_name = ",last_name)
        print("birthday = ",birthdate)
        email_enter = input("enter email address =")
        b = email_address(email_enter)
        print("email_address = ",b)
        password_enter = input("enter the password")
        c1 = password_checker(password_enter)
        print(c1)
    elif option == 2:#login code
        email_enter = input("enter email address =")
        b = email_address(email_enter)
        print("email_address = ",b)
        password_enter = input("enter the password")
        c1 = password_checker(password_enter)
        print(c1)
        username_email_id = input("Please enter your username : ")
        password = input("Please enter your password : ")
        if username_email_id == email_enter and password == password_enter:
            print("login successfully!!!")
        else:
            print("login failed!! please enter correct email_id and password")
    else:
        print("exist")
        break 
def login_successfully(update_first_name,update_last_name,update_email_address):
    return update_first_name
    return update_last_name 
    return update_email_address 


while True:
    print("1. update details")
    print("2. delete profiles")
    print("3. exist")
    Registration_form(first_name,last_name,email_address)
    
    
    update_option = int(input("enter the option you want to update ="))
    if update_option == 1:
        update_first_name = input("enter the first_name you want to update =")
        update_last_name = input("enter the last_name you want to update =")
        update_email_address = input("enter the email you want to update =")
        
        
        a = login_successfully(update_first_name,update_last_name,update_email_address)
        print(update_first_name)
        print(update_last_name)
        print(update_email_address)
        
        
    else:
        print("exist")

    
        
    

  
    
    









