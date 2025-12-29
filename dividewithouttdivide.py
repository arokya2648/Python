#Programe to ddiovide 2 numbers wihtout using the doivide function
def divide(ourdivident, ourdivisor):
    #Check if divisor is +ve or -ve
    sign=(-1 if((ourdivident<0)^(ourdivisor<0)) else 1)
    #make both positive
    ourdivident=abs(ourdivident)
    ourdivisor=abs(ourdivisor)
    quotientnumber=0
    tempnumber=0
    # go from 31 to 0 and accumulate all valid bits
    for i in range(31, -1, -1):
        if (tempnumber + (ourdivisor<<i) <= ourdivident):
            tempnumber +=ourdivisor <<i
            quotientnumber |= 1 <<i
    # Assuming the sign value computed earlier is -1, negate the quotient value
    if sign ==-1 :
        quotientnumber=-quotientnumber
    return quotientnumber
a = int(input('Enter a for a/b:'))
b = int(input('Enter b for a/b:'))
print('Result of',a,'/',b,'is',divide(a, b))