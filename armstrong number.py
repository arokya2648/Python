number=int(input('Input your number'))
digits=len(str(number))
resultnumber=0
temp=number
while temp>0:
    digit=temp%10
    resultnumber+=digit**digits
    temp//=10
if number==resultnumber:
    print(number, ('Is an armstrong number'))
else:
    print(number, 'is not an armstrong number')