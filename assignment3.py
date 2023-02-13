def format_amount(amount):
    '''
    this is a doctring 
    
    '''
    return f'{amount}.00'
def convert_in_words(num):
    if num == 0:
        return "zero"
    ones = ["","one","two","three","four","five","six","seven","eight","nine"]
    tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    teens = ["ten","eleven","twelve","thirtheen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    empty_string = ""
    while num >0:
        if num<10:
            empty_string+= ones[num]
            num = 0 
        elif num>=10 and num<20:
            empty_string+= teens[num%10]
            num = 0 
        elif num<100:
            empty_string+= tens[num//10]
            if num%10!=0:
                empty_string+= "-"+ones[num%10]
                num = 0 
        else:
            empty_string+= ones[num//100]+" hundred "
            num%=100 
    return empty_string
amount = int(input("enter the number which is less than 1000="))
print(amount,convert_in_words(amount))
                