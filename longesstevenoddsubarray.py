def longestevenoddsubarray(arr, n):
    longest=1
    cnt=0
    for i in range(n-1):
        if ((arr[i] + arr[i+1])%2==1):
            cnt=cnt+1
        else:
            longest=max(longest, cnt)
            cnt=1
    if (longest==1):
        return 0
    return max(cnt, longest)
arr=[3, 2, 4, 3, 2, 3, 3, 3, 2, 3, 2, 3, 2, 4, 2]
n=len(arr)
print(longestevenoddsubarray(arr, n))