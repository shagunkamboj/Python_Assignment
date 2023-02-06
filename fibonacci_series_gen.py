def fibo(n):
    a = 0 
    b = 1 
    if n == 1 :
        yield a 
        # print(a)
    elif n == 2 :
        # print(b)
        yield b       
    else:
        yield a,b
        # print(a,b,end = " ")   
                
        for i in range(n-2):
            c = a+b
            a = b
            b = c
            yield a,b
            # print(a,b,end = " ")     
fibo(7)
