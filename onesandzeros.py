def numberofbits(n):
    ones=0
    zeros=0
    #Whilw our number is greater than zero check ones and zeros and right shift
    while(n):
        #use and operator to check if last number is 1 or 0
        if(n&1==1):
            ones+=1
        else:
            zeros+=1
        #right shift the number to remove the last bit we just checked
        n>>=1
    print('\n\nOnes=',ones,'\nZeros',zeros)
number=int(input('Enter your number'))
numberofbits(number)