print('Select your ride')
print('1. Bike')
print('2. Car')
choice=int(input('Enter your choice:'))
if(choice==1):
    print('What type of bike?')
    print('1. scooty')
    print('2. Motorcycle')
    choice2=int(input('Enter your choice2:'))
    if choice2==1:
        print('You have selected scooty')
    else:
        print('You have selected motorcycle')
elif(choice==2):
    print('What type of car?')
    print('1. Sedan')
    print('2. XUV')
    choice3=int(input('Enter your choice3:'))
    if choice3==1:
        print('You have selected Sedan')
    else:
        print('you have selected XUV')
else:
    print('wrong choice')