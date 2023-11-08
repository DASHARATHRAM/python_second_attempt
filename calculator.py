# calculator


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    num1 = float(input("What is your number? "))
    for symbol in operations:
        print(symbol)
        
    continue_y = True
    while continue_y:
        operation_symbol = input("What do you wann do? ")
        num2 = float(input("What is your next number? "))
        func = operations[operation_symbol]
        answer = func(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        to_continue = input(f"Type 'y' to conitnue calculating with or type 'n' to start new calculation: ")
        if to_continue == 'y':
            num1 = answer
        elif to_continue == 'n':
            continue_y = False
            calculator()
        else:
            print("invalid reponse")
calculator()
