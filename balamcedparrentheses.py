def paren(s,l,r,p,n):
    #if we reach end of the list just print it and return it
    if(p==2*n):
        for ss in s:
            print(ss,end='')
        print('\n')
        return
    #if left parentheses is greater than we can print right one
    if(l>r):
        s[p]='}'
        paren(s,l,r+1,p+1,n)
    #left parentheses should not exceed n
    if(l<n):
        s[p]='{'
        paren(s,l+1,r,p+1,n)
n=int(input('Enter number of parentheses'))
s=['']*2*n
print('n')
paren(s,0,0,0,n)