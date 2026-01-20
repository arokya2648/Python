#program to find all the possible combinations when we press keys in phone keppad
keypad=["","", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
def printcombination(combination, curr, output, n):
    if(curr==n):
        print(*output,sep=",")
        return
    #Print all possible combinations by iterating first 1 to 3 for number and finding that index in keypad\
    for i in range(len(keypad[combination[curr]])):
        output.append(keypad[combination[curr]][i])
        printcombination(combination, curr + 1, output, n)
        output.pop()
        if(combination[curr]== 0 or combination[curr]==1):
            return
combination=[4, 3, 4]
n=len(combination)
printcombination(combination, 0, [], n)