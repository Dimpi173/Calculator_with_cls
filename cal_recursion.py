import os


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1/num2


operation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


def calculator():
    first_number = float(input("Enter first number : "))
    stop = False
    while not stop:
        for i in operation:
            print(i)
        operator = input("pick an operator : ")
        second_number = float(input("Enter second number : "))
        result = operation[operator](num1=first_number, num2=second_number)
        print(f"{first_number} {operator} {second_number} = {result}")
        print(f"Enter 'y' to continue with {result} or 'n' to start a new calculation or 'x' for exit : ", end="")
        user_choice = input().lower()
        if user_choice == "y":
            first_number = result
            continue
        elif user_choice == "n":
            os.system('cls')
            stop = True
            calculator()
        elif user_choice == "x":
            stop = True
        else:
            print("Somthing went wrong")
            stop = True


calculator()
print("Thank you for using our calculator")
