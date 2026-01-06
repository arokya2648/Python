#Program to print numbers  decreasing then increasing
def incdec(n, num):
    #Base case to return the value when we reach our limit
    if(n<1 or n>num):
        return
    #Print decreasing first
    print(n)
    incdec(n-1, num)
    #Print increasing order
    print(n)
n=int(input('Enter any number n: '))
incdec(n, n)