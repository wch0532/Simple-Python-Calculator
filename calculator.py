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

# 运行示例
if __name__ == "__main__":
    try:
        a = 10
        b = 5
        op = '+'

        result = calculate(a, b, op)
        print(f"Calculation: {a} {op} {b} = {result}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
