def charoccurance(inputstr,ch): #user define Function
    occurance = 0;
    for i in range(0,len(inputstr)):
        if(inputstr[i] == ch):
            occurance+=1
            
    return occurance

print("Occurance of character in a string...")
inputstr=input("Enter String : ")
ch=input("Enter Character : ")
print(charoccurance(inputstr,ch))
        
