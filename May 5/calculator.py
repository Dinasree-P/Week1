# Define a function named 'calculator'
def calculator():
    # Display available operations to the user
    print("Select operation: +, -, *, /")

    # Prompt the user to enter an operator
    op = input("Enter operator: ")

    # Get the first number from the user and convert it to float
    a = float(input("Enter first number: "))

    # Get the second number from the user and convert it to float
    b = float(input("Enter second number: "))

    # Perform addition if the operator is '+'
    if op == '+':
        print("Result:", a + b)

    # Perform subtraction if the operator is '-'
    elif op == '-':
        print("Result:", a - b)

    # Perform multiplication if the operator is '*'
    elif op == '*':
        print("Result:", a * b)

    # Perform division if the operator is '/'
    elif op == '/':
        if b != 0:  # Check for division by zero
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        # Handle invalid operator input
        print("Invalid operator")

# Call the calculator function to execute the program
calculator()
