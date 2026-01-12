def checksorted(a):
    #Calculating length of array
    length=len(a)
    #if array length is 0, 1 means we need not to check further
    if length==1 or length==0:
        return True
    #Return true if both below conditions are true
    return a[0]  <= a[1] and checksorted(a[1:])
a = [1,2,3,4,5,8,2]
#displaying result
if checksorted(a):
    print('\nYes given array is sorted')
else:
    print('\n No given array is not sorted')