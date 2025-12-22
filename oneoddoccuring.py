#programe to find the element not makning a pair
#function to claculate the number that is odd occurring
def oddoccurring(arr):
    #initialize result
    res=0
    #traverse the arrray
    for element in arr:
        #XORR with result
        res=res^element
    return res
#initialize our array
arr=[]
#take array size as input
n=int(input('Enter arrray size:'))
#take aaray element input
while(n):
    num=int(input('Enter number:'))
    arr.append(num)
    n-=1
print('\n\nOdd occurring number is:', oddoccurring(arr))