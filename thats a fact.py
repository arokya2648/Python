def printfactors(number):
    print('the factors of', number ,"are:")
    for i in range(1, number+1):
        if number%i==0:
            print(i)
number=int(input('Enter your number to find its factors'))
printfactors(number)