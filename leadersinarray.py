def leaders(a, a_size):
    #right most is always leader
    currentmax=a[a_size-1]
    print(currentmax)
    #check from second last element if it is greater than currentmax if yes number is the new leader and currentmax
    for i in range(a_size-2, -1, -1):
        if currentmax < a[i]:
            print(a[i])
            currentmax=a[i]
a=[16,17,4,3,5,245]
leaders(a, len(a))