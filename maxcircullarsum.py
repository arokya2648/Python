#standard kaden's algorrriuth to find naximum subarray sum
def kadane(a):
    n=len(a)
    maxsofar=0
    maxendinghere=0
    for i in range(0, n):
        maxendinghere=maxendinghere+a[i]
        if (maxendinghere<0):
            maxendingherre=0
        if (maxsofar<maxendinghere):
            maxsofar=maxendinghere
    return maxsofar
#the function returns maximum circular contiguous sum in 
#a[]
def maxcircularsum(a):
    n=len(a)
    #apply kadane algo if not circular is needed
    max_kadane=kadane(a)
    #find sum of all element and invert them
    max_wrap=0
    for i in range(0, n):
        max_wrap+=a[i]
        a[i]=-a[i]
    #apply kadance algo to find minimum inverted subarray
    max_wrap=max_wrap+kadane(a)
    #the maximum circular sum will be a maximum of 2 sums
    if max_wrap>max_kadane:
        return max_wrap
    else:
        return max_kadane
a=[11, 10, -20, 5, -3, -5, 8, -13, 10]
print('Maximumn circular sum is ', maxcircularsum(a))