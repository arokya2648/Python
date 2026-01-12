def arraytotalsum(a):
    #Calculating length of array
    length = len(a)
    #if arrrray length is 1 just return the element
    if length==1:
        return a[0]
    #return curent element and received sum
    return a[0] + arraytotalsum(a[1:])
a=[1,2,3,6]
#Display resullt
print('Array total sum:', arraytotalsum(a))