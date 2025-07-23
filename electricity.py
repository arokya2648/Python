u=int(input("Please enter the number of units you consumed:"))
if(u<50):
    amount=u*2.60
    surcharge=25
elif (u<=100):
    amount=130+((u-50)*3.25)
    surcharge=35
elif (u<=200):
    amount=130+162.5+((u-100)*5.26)
    surcharge=45
else:
    amount=130+162.5+526+((u-200)*8.45)
    surcharge=75
total=amount+surcharge
print('\nElectricity Bill=%.2f' %total)