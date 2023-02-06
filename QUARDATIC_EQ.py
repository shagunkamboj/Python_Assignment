import cmath 
b = int(input("enter the value of b ="))
a = int(input("enter the value of a ="))
c = int(input("enter the value of c ="))
d = b**2 - 4*a*c
d2 = (-b - cmath.sqrt(d))/(2*a)  
d1 = (-b + cmath.sqrt(d))/(2*a) 

print(abs(d1))
print(abs(d2))