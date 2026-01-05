#Prrogram to fing  the factorial of any number using recursion
def fac(n):
    #When n =1 or 0 return 1
    if(n==1 or n==0):
        return 1
    #factorial of n=n*n-1*n-2*n-3.......1
    return n*fac(n-1)
n=int(input('Enter the number you want to find the factorial of'))
print('Factorial  of', n ,'is:', fac(n))