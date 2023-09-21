def swap(a,b): #user define Function
    a=a+b
    b=a-b
    a=a-b

    print("X : ",a,"\nY : ",b)

print("Swap two number....")
x=int(input("Enter Number 1 : "))
y=int(input("Enter Number 2 : "))
swap(x,y)
