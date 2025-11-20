def fun1(n):
    return n*(n+1)/2
print (fun1(4))
print('so, the number of iterations will be 1 forr any input')
def fun2(n):
    sum=0
    for i in range(1, n+1):
        sum+=i
    return sum
print(fun2(4))
print('so, the number of iterations will be 1+1+1+1=4=n(input) iterations')
def fun3(n):
    sum =0
    for i in range(1,n+1):
        for j in range(1, i+1):
            sum+=1
    return sum
print(fun3(4))
print('So, the number of iterations will be 1+2+3+4=10')