#Program to print numbers 1 to 10 using reucurssion
#Recurssive function that will accept n till we reach 10
def print1to10(n):
    if(n>10):
        return
    print(n)
    #Recursive call from 1 to 2 2 to 3 3 to 4 and  so  on
    print1to10(n+1)
print1to10(1)