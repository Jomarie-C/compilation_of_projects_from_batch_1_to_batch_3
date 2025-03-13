num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 < num2:
    print(num1 , "is smaller than", + num2)
elif num2 < num1:
    print(num2 , "is smaller than", + num1)
elif num1 == num2:
    print("Both numbers are equal.")