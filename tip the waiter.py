def totalcalc(billamount,tipperc):
    total=billamount*(1+0.01*tipperc)
    total=round(total,2)
    print(f'Please pay${total}')
totalcalc(150,30) 