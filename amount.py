l = [2000,1000,500,200,100,50,10,5,2,1]
amount = int(input("enter the total number of amount in your account ="))
for i in l:
    if amount>1:
        a = amount//i    
        print("amount =", i," ",'number of notes available ',a)
        amount = amount%i








# amount = int(input("enter the amount you want ="))

# def total(list1,amount):
#     for i in list1:
#         start = 0 
        
#         if amount>=i:
#             if i == 2000:
#                 start = amount//i
                
#                 amount = amount %i
#                 return start 
            
# list1 = [2000,1000,500,200,100,50,10]

# m = total(list1,amount)
# print(m)



            
        