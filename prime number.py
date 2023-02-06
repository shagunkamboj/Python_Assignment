lower_limit = 1 
upper_limit = 1881 
for i in range(lower_limit,upper_limit+1):
    if i >1 :
        for j in range(2,i):
            if i%j == 0:
                break 
        else:
            print(i)
print("***********prime nu7mber using functions****************")
def prime_number(lower_limit,upper_limit):
    for i in range(lower_limit,upper_limit+1):
        if i >1 :
            for j in range(2,i):
                if i%j == 0:
                    break 
            else:
                print(i)
lower_limit = 0 
upper_limit = 100 
prime_number(lower_limit,upper_limit)
    
    