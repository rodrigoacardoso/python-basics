num = int(input("Insert an number: "))
if num<2:
    print (num, "is not a prime number")
else:
    i=0
    d=0
    while (i<num):
        i=i+1
        if (num%i==0):
            d=d+1
    if (d>2):
        print(num, "is not a prime number.")
    else:
        print(num, "is a prime number.")
    
    
  
     
  
