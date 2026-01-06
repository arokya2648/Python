def xyz(n):
    n=int(input('Enter a number'))
    if n>0:
        print('Positive number')
        xyz(n)
    elif n==0:
        print('zero')
        xyz(n)
    else:
        print('Negative number')
xyz(9)