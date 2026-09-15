def arithmetic(a, b, operator):
    match operator:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            if b != 0:
                return a / b
            return "Cannot divide by zero"
        case '%':
            return a % b
        case '**':
            return a ** b
        case _:
            return "Invalid operator"


# Taking input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, %, **): ")

result = arithmetic(a, b, operator)

print("Result:", result)