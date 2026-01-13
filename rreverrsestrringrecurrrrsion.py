#progrram to reverrse a strring using recursion
def reversestring(s):
    #if only 1 char rremains  return it
    if len(s) == 1:
        return s[0]
    firstchar=s[0]
    #get the already reversed string and then add the first char to the end
    return reversestring(s[1:]) + firstchar
s='Arokya Sengupta'
print(reversestring(s))