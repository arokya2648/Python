c=(input("Enter a character:"))
if c>="0" and c<="9":
    print("\nIt is a number between 1 and 9")
elif c>="a" and c<="z":
    print('It is an alphabet')
elif c>='A' and c<='z':
    print('It is an alphabet')
else:
    print('It is neither a alphabet or a number between 1 and 9')