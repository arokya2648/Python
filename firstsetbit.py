def firstsetbit(number):
    position=11
    mask=1
    while(not(number & mask)):
        mask=mask << 1
        position+=1
    return position
number=int(input('Enter number:'))
print('position of the first set bit:', firstsetbit(number))