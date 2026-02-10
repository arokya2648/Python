#program to find trthe maximum  consecutive 1s in an array of 1's and 0's
#returhnsb tthe result
def getmaxlength(a, a_size):
    counter=0
    maxones=0
    for i in range(0, a_size):
    #if we find a=0 then rresett the counter
        if(a[i]==0):
           counter=0
    #if we find 1 then increment the counter and update the maxones
        else:
          #incrrease countt
          counter+=1
          maxones=max(maxones, counter)
    return maxones
a=[1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
a_size=len(a)
print('Max 1s:', getmaxlength(a, a_size))