print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f


mode = input("Enter mode (+, -, *, /, CF): ")
if mode in ['+', '-', '*', '/']:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if mode == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif mode == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif mode == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif mode == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
elif mode == 'CF':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius} Celsius is equivalent to {fahrenheit} Fahrenheit")
else:
    print("Invalid mode selected.")