def swap(a,b): #user define function
    a=a+b
    b = a[0 : (len(a) - len(b))] #slicing of String using array slicing method,you can also use inbuilt slice() method.
    a = a[len(b):]  

    print("X : ",a,"\nY : ",b)

print("Swap two String....")
x=input("Enter String 1 : ")
y=input("Enter String 2 : ")
swap(x,y)
