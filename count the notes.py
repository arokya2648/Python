amount=int(input("Please enter the amount for withdrawl:"))
note_1=amount//100
note_2=(amount%100)//50
note_3=((amount%100)%50)//10
print("notes of 100 rupees:", note_1)
print('Notes of 50 rupees:', note_2)
print ('Notes of 10 rupees:', note_3)