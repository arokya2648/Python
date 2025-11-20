def o1(n, m):
    total=n*m
    print('1 iteration: 1')
def o2(n, m):
    total=0
    for i in range(1, n+1):
        total+=m
    print('N iteration:', n)
m=int(input('Enter an a for a*b:'))
n=int(input('Enter a b for a*b:'))
o1(m, n)
o2(m, n)