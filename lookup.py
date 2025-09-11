class pair_elements:
    lookup={}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return (lookup[target - num],1)
        lookup[num] = i
value=int(input('Enter sum for which you want to make this search : '))