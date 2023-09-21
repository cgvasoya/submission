def bigsmallnumber(arr):#user define function
    l = len(arr)
    #default min and max is 0
    minnum=arr[0] 
    maxnum=arr[0]
    

    for i in arr: #iterate over Array.

        if(minnum>i):
            minnum=i

        if(maxnum<i):
            maxnum=i

    print("Maximum is: ",maxnum,"\nMinimum is: ",minnum)

print("Largest and smallest number from array....")
bigsmallnumber([-1,55,3,34,5,62,7,8])
