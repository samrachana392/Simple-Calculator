# Simple calculation for basic operation as my first python project
print("1 - Addition")
print("2 - subtraction")
print("3 - Multiplication")
print("4 - Division")

option=int(input("Enter your choice: "))
if (option in [1,2,3,4]):
    num1=int(input("Enter First Number: "))
    num2=int(input("Enter Second Number: "))

    if option == 1:
        result=num1+num2
    elif option == 2:
        result = num1-num2
    elif option == 3:
        result = num1 * num2
    elif option ==4:
       if(num2==0):
           print("second number can't be 0")
       else:
           result=num1/num2
       
else:
    print("Invalid Input")

print("Result of the operation is ", result)
