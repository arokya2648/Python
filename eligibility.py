mc=input("Do you have a medical cause y or n:")
at=int(input('enter the attendence of the student: '))
if mc=="y":
    print('you are allowed')
else:
    if at>=75:
        print('allowed')
    else:
        print('Not allowed')