def checkifsame(number1, number2):
    if ((number1^number2)!=0):
        print('The two numbers are not equal')
    else:
        print('The two numbers are equal')
number1=int(input('Enter the first number'))
number2=int(input('Enter the second number'))
checkifsame(number1, number2)