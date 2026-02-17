#Program to find the equilibrrium index for an array index
def equilibriumpoint(arr):
    leftsidesum=0
    rightsidesum=0
    n=len(arr)
    #go to each index in the array and check if it iss an equilibrium point
    for i in range(n):
        leftsidesum=0
        rightsidesum=0
        #get left sum
        for j in range(i):
            leftsidesum+=arr[j]
        #get right sum
        for j in range(i+1, n):
            rightsidesum+=arr[j]
        #if left sum and right sum are same, then we are done
        if leftsidesum==rightsidesum:
            return i
    return-1
arr=[-4,6,2,0,0,1,1]
print('Element:',arr[equilibriumpoint(arr)])