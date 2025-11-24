def onsquaretime(n):
    iterations=0
    for i in range(0, n):
        for j in range(0, n):
            print('*', end=' ')
            iterations+=1
        print('')
    print('When  n is',n,'Iterations=', iterations)
onsquaretime(5)
onsquaretime(4)
onsquaretime(3)
print('With every n the time taken equals n^2')
print('O(n^2)')       