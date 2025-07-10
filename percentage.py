print("Enter marks obtained in 4 subjects")
math=int(input("Maths:"))
science=int(input("Science:"))
english=int(input("English:"))
hindi=int(input('Hindi:'))
sum=math+science+english+hindi
print("Sum of marks of the 4 subjects is:", sum)
percentage=(sum/400)*100
print("Percentage mark:", percentage)