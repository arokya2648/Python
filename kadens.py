#program to find max subarray sum
def maxsubarraysum(a, a_size):
    max=-99999999999
    cmax=0
    #add current element to currentmax, check if cmax>mnax, if yes update max, if  cmax is less than 0 then rresset it to 0
    for i in range(0, a_size):
        cmax=cmax+a[i]
        if (max<cmax):
            max=cmax
        if cmax<0:
            cmax=0
    return max
a=[1,2,3,-4,5,-22,-4,25,2,-9]
print(maxsubarraysum(a, len(a)))    