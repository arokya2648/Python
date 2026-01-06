def headrec(n, num):
    #Base case, if n exceeds num terminate the recursion
    if n>num:
        return
    #Recursive call with the next value
    headrec(n+1, num)
    #Print the current value of n after returning the recursive call
    print(n)
#promt the user to enter the value of n
n=int(input('Enter the  value of n to print 1 to n:'))
#initialize call to the headrec function starting from 1
headrec(1, n)