age = int(input("how old are you?:"))
if age > 10 and age < 20:
    print("you are allowed in class age limit in between 10 and 20")
elif age < 10 or age > 20:
    print("you are not allowed in class")