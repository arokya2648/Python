def tailrec(n, num):
    #Base case if n exceeds number terminate function
    if n>num:
        return
    #print the current value of n
    print(n)
    #Recurrrsive call with  the next value(Tail recursion)
    tailrec(n+1, num)
#Prompt the user to enter the value of n
n=int(input('Enter n to print 1 to n:'))
#initialize call to  tthe tailrec function starting from 1
tailrec(1, n)