# Lab 1: Conditions and Dynamic Calculator


def check_number(number):
    if number < 0:
        number = 0
        print("Negative changed to zero")
    elif number == 0:
        print("Zero")
    elif number == 1:
        print("Single")
    else:
        print("More")


def calculator():
    print("\nDynamic Calculator")
    print("Enter an expression such as 1 + 2 * 3")
    print("Press Enter without typing anything to stop.")

    while True:
        expression = input("Expression: ")
        if expression == "":
            break
        try:
            answer = eval(expression, {"__builtins__": {}}, {})
            print("Answer:", answer)
        except Exception:
            print("Please enter a correct arithmetic expression.")


try:
    number = int(input("Please enter an integer: "))
    check_number(number)
    calculator()
except ValueError:
    print("Please enter a valid integer.")
