def hcf(numbersmallest, numberlargest):
    while(numbersmallest):
        numberstore=numbersmallest
        numbersmallest=numberlargest%numbersmallest
        numberlargest=numberstore
    return numberlargest
numberlargest=int(input('Enter the largest  number'))
numbersmallest=int(input('Enter the smallest  number'))
lcm = int((numbersmallest / hcf(numbersmallest, numberlargest))*numberlargest)
print('LCM is:', lcm)