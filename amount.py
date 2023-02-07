l = [2000,1000,500,200,100,50,10,5,2,1]
amount = int(input("enter the total number of amount in your account ="))
for i in l:
    if amount>1:
        a = amount//i    
        print("amount =", i," ",'number of notes available ',a)
        amount = amount%i