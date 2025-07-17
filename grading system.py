print('Enter the marks obtained in 5 subjects:')
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
tot=a+b+c+d+e
avg=tot/5
if avg>=91 and avg<=100:
    print("Your grade is A1")
elif avg>=81 and avg<91:
    print("Your grade is A2")
elif avg>=71 and avg<81:
    print("Your grade is B1")
elif avg>=61 and avg<71:
    print("Your grade is B2")
elif avg>=51 and avg<61:
    print("Your grade is c1")
elif avg>=41 and avg<51:
    print("Your grade is C2")
elif avg>=33 and avg<41:
    print("Your grade is D")
elif avg>=21 and avg<33:
    print("Your gradeis E1")
elif avg>=0 and avg<21:
    print("Your grade is E2")
else:
    print("invalid inout")