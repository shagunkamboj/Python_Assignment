# num = 10
# i = 1 
# count = 0 
# while i <=num:
#     if num%i == 0:
#         count+=1 
#     i+=1 
# if count == 2:
#     print("no is prime")
# else:
#     print("not")
    
print("*************prime number using generator*************")  
def prime_number(num):
    i = 1
    count = 0 
    while i <=num:
        if num%i == 0:
            count+=1 
        i+=1 
    if count == 2:
        yield "no is prime"
    else:
        yield "not prime"
y = prime_number(12)
print(next(y))
