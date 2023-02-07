# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

#lambda function in python 
# sum of two number in python
lambda_function = lambda a,b : a+b 
print(lambda_function(2,3))


#sum of 3 numbers using lambda
lambda_function = lambda a,b,c : a+b+c
print(lambda_function(2,3,66))


#lambda function using python functions 
def fun(n):
    return lambda a:a*n    
my_double = fun(3)
print(my_double(11))