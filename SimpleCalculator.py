operation =input("Choose one of the following operations: +, -, * or /")
num1 = float(input("Introduce the first number: "))
num2= float(input("Introduce the other number: "))
if (operation == "+"):
    result=num1+num2
    print(result)
if (operation == "-"):
    result=num1-num2
    print(result)
if (operation == "*"):
    result=num1*num2
    print(result)
if (operation == "/"):
    if (num2!=0):
        result=num1/num2
        print(result)
    else:
        print("Error: Divided by 0")
else:
    print("Invalid operation")