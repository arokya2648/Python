numberlargest=int(input('Enter the largest  number'))
numbersmallest=int(input('Enter the smallest  number'))
while(numbersmallest):
    numberstore=numbersmallest
    numbersmallest=numberlargest%numbersmallest
    numberlargest=numberstore
print('HCF is:', numberlargest)