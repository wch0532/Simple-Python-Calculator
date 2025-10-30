# calculator.py

def calculate(num1, num2, operation):
    """
    执行基本的四则运算。
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # 确保不会出现除以零的错误
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        return num1 / num2
    else:
        return "Error: Invalid operation!"

def get_number_input(prompt):
    """Prompts the user for a number, handling invalid input until a valid float is entered."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# 运行示例
if __name__ == "__main__":
    try:
        num1 = get_number_input("Enter the first number: ")

        valid_operators = ['+', '-', '*', '/']
        operator = ""
        while operator not in valid_operators:
            operator = input(f"Enter the operator ({', '.join(valid_operators)}): ")
            if operator not in valid_operators:
                print(f"Invalid operator. Please choose from {', '.join(valid_operators)}.")

        num2 = get_number_input("Enter the second number: ")

        # The calculate function already handles division by zero and invalid operators.
        result = calculate(num1, num2, operator)

        # Print the result or the error message from the calculate function
        if isinstance(result, str) and result.startswith("Error:"):
            print(result)
        else:
            print(f"Result: {num1} {operator} {num2} = {result}")

    except KeyboardInterrupt:
        print("\nCalculation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")