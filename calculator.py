def add(p,q):
    #This function is used for adding 2 numbers
    return p+q
def substract(p,q):
    #This function is used for substracting 2 numbers
    return p-q
def multiply(p,q):
    #this function will multiply 2 numbers
    return p*q
def divide(p,q):
    #this function will divide 2 numbers
    return p/q
def exponential(p,q):
    return p**q
#now we take inputs from the user
print('Please select a operation:')
print('a, add')
print('b, substract')
print('c, multiply')
print('d, divide')
print("e, exponential")
choice=input('Please enter choice(a/b/c/d/e):')
num1=int(input('Please select the first number:'))
num2=int(input("Please select the second number:"))
if choice=="a":
    print(num1,"+",num2,"=", add(num1,num2))
elif choice=='b':
    print(num1,"-",num2,"=", substract(num1,num2))
elif choice=='c':
    print(num1,"*",num2,"=", multiply(num1,num2))
elif choice=='d':
    print(num1,"/",num2,"=", divide(num1,num2))
elif choice=='e':
    print(num1,"to the power of",num2,"=", exponential(num1,num2))
else:
    print('This is an invalid input')