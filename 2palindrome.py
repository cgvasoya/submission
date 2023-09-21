def palindromestr(inputstr): #user define function
    res = False
    l = len(inputstr)
    for i in range(0,l-1):
        l-=1
        if(inputstr[l] == inputstr[i]):
            res = True
        else:
            res = False
        
    return res

print("Palindrome String.....")
inputstr=input("Enter String : ")
print(palindromestr(inputstr))
