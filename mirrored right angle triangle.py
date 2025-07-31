r=int(input("please enter the total number of rows:"))
print('Mirrored right angle triangle star pattern')
for i in range(1, r+1):
    for j in range(1, r+1):
        if(j<=r-i):
            print(' ',end=" ")
        else:
            print("*", end=" ")
    print()