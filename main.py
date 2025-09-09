num=int(input('You want odd or even number under what value;'))
odd_list=[i for i in range(num) if i%2 !=0]
print('list of odd numbers', odd_list, '\n')
even_list=[i for i in range(num) if i%2==0]
print('list of odd numbers', even_list, '\n')
fruits=['apple', 'banana', 'mango', 'papaya', 'grapes']
fruits=[x[0].upper() + x[1:] for x in fruits]
print('fruits as proper nouns;', fruits)