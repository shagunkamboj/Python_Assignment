ones = ["","one","two","three","four","five","six","seven","eight","nine"]
tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
teens = ["ten","eleven","twelve","thirtheen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
empty_string = ""
amount = int(input("enter the amount ="))
def format_amount(amount):
    '''
    this is a doctring 
    
    '''
    return f'{amount}.00'
def convert_in_words(num,amt):
    
        
        for_amount = num(amt)
        n = int(float(for_amount))
        if n == 0:
            return "zero"
        else:
   
            while n >0:
                empty_string = ""
                if n<10:
                    empty_string+= ones[n]
                    n = 0 
                elif n>=10 and n<20:
                    empty_string+= teens[n%10]
                    n= 0 
                elif n<100:
                    empty_string+= tens[n//10]
                    if n%10!=0:
                        empty_string =empty_string+"-"+ones[n%10]
                        n = 0 
                else:
                    empty_string+= ones[n//100]+" hundred "
                    n%=100 
            
            return empty_string
    
format_amount = convert_in_words(format_amount,amount)
print(format_amount)
                