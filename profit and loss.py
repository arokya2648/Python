s=float(input("Please enter the amount the product is sold for"))
c=float(input("Please enter the amount the product is bought for"))
if(s>c):
    amount=s-c
    print('Total profit=', amount)
else:
    amount2=c-s
    print("Total loss=", amount2)