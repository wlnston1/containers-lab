def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mult (a,b):
    return a * b

def div (a, b):
    return a / b

op = input("What calculation would you like to do?").lower()
num1 = int(input("What is number 1?"))
num2 = int(input("What is number 2?"))

if op == "add":
    print(f'The result is {add(num1, num2)}')

if op == "sub":
    print(f'The result is {sub(num1, num2)}')

if op == "mult":
    print(f'The result is {mult(num1, num2)}')

if op == "div":
    print(f'The result is {div(num1, num2)}')