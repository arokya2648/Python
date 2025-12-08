number=int(input('Enter yourr number:'))
originalnumber=number
reversednumberr=0
while number>0:
    digit=number%10
    reversednumber=reversednumberr*10+digit
    number//=10
if originalnumber==reversednumber:
    print(originalnumber, 'Is a palindrome')
else:
    print(reversednumber, 'Is a plindrome')