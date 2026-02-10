#progrram to move the serrox to tthe end
def pushzerostoend(a, a_size):
    #zerro will hold the position where non zero numbers should be
    zero=0
    #non zerro will iterate to find if the current number is zero or non zerro
    nonzero=0
    while(nonzero!=a_size):
        if a[nonzero]!=0:
            a[nonzero],a[zero]=a[zero],a[nonzero]
            zero+=1
        nonzero+=1
#driver code
a=[1,0,3,6,0,0,0,2,355,0,72]
a_size=len(a)
print(a)
pushzerostoend(a, a_size)
print('Array afterr pushing all the zeros to the end of the arrray')
print(a)