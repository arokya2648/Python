valid=False
while not valid:
    try:
        n=int(input('Enter an even number:'))
        while n%2==0:
            print('BYE')
        valid=True
    except ValueError:
        print('invalid')