total_amount=int(input('Enter yourr total amount'))
listofnotes=[1000,500,100,50,20,10,5]
for i in listofnotes:
    numberofnotes=total_amount//i
    total_amount%=i
    if numberofnotes !=0:
        print(f'The number of notes of {i} is {numberofnotes}')