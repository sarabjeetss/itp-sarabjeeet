# First I will take input from the user
def takeInput():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator (+,-,*,/): ")
    return num1, num2, operator

# Second is function to perform calculations and display result
def displayResult(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        print("Invalid operator")
        return
    print(f"{num1} {operator} {num2} = {result}")

#This one is  main program
num1, num2, operator = takeInput()
displayResult(num1, num2, operator)