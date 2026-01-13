#Program to reverrse a number using recursion
def reversenumber(num):
    if(num>0):
        #if the num is not 0 then get the last digit and add to the currrent rreverrsed number rreceived
        last=num%10
        if(num//10>0):
            current_number=reversenumber((int)(num //10))
            return last*pow(10,len(str(current_number))) + current_number
        return num
n=int(input('Enter the number you want to  reverse'))
print('Reversed:', reversenumber(n))