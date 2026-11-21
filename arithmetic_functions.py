def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b


def modulus(a, b):
    if b == 0:
        return "Modulus by zero is not possible"
    return a % b


def power(a, b):
    return a ** b


def floor_divide(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a // b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
print("Modulus:", modulus(a, b))
print("Power:", power(a, b))
print("Floor Division:", floor_divide(a, b))
