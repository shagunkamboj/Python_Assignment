# def Area(length,breadth):
#     return length*breadth 
# def Area(length,breadth,height):
    
#     return length*breadth*height 
# m = Area(2,3)
# print(m)
# m1 = Area(2,3,4)
# print(m1)


#2 METHOD

def add(a = None,b = None):
    if a!=None and b == None:
        return a
    else:
        return a+b 
obj1 = add(2,3)
print(obj1)
obj2 = add(2)
print(obj2)




# argss
def Function_overloading(*args):
    
    for i in args:
        print(i)
        
Function_overloading(2,3)
Function_overloading(2,3,4)

def Function_overloading(*args):
    sum = 0 
    for i in args:
        sum = sum + i 
    print (sum)
        
Function_overloading(2,3)
Function_overloading(2,3,4)



#KWARGS
def Function_overloading(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
Function_overloading(first = 2,last = 4)
Function_overloading(first = 2,mid = 5 ,last = 4)



         

