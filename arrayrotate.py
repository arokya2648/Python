#program to rotate an array'n' times to the left
#input array length and 'n'
def rotations(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)
#rotate array to the left by one place
def rotate(a, a_size):
    temp=a[0]
    for i in range(a_size-1):
        a[i]=a[i+1]
        a[a_size-1]=temp
def printarray(a, a_size):
    for i in range(a_size):
        print('%d'% a[1], end=' ')
    print('\n')
a=[12,12,31,85,2,3,53,5632]
printarray(a, len(a))
rotations(a, 2, len(a))
printarray(a, len(a))