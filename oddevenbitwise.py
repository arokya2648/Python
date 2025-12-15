def isevenodd(n):
    if (n^1==n+1):
        return True
    else:
        return False
number=int(input('Enter your number'))
if isevenodd(number):
    print(number,'Is even')
else:
    print(number,' Is odd')