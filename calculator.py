from pyfiglet import Figlet


def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Can not divide by Zero!")
    else:
        return a / b


def power(base, exponent):
    return base ** exponent


calculatorText = Figlet()
byeText = Figlet()
print(calculatorText.renderText("Python Calculator"))

while True:
    try:
        insertedNumber = int(input("1. Start Calculator" + "\n" + "2. Exit Calculator\n"))
        if insertedNumber == 1:
            selectedNumber = int(input(
                "To proceed, please choose one of the following operations below:" + "\n" + "1 - Sum" + "\n" + "2 - Subtract" + "\n" + "3 - Multiply" + "\n" + "4 - Divide" + "\n" + "5 - Power" + "\n" + "6 - Exit\n"))

            if selectedNumber == 1:
                firstValue = int(input("Enter the first value: \n"))
                secondValue = int(input("Enter the second value: \n"))
                print("The result of the Operation is: ", sum(firstValue, secondValue))
            elif selectedNumber == 2:
                firstValue = int(input("Enter the first value: \n"))
                secondValue = int(input("Enter the second value: \n"))
                print("The result of the Operation is: ", subtract(firstValue, secondValue))
            elif selectedNumber == 3:
                firstValue = int(input("Enter the first value: \n"))
                secondValue = int(input("Enter the second value: \n"))
                print("The result of the Operation is: ", multiply(firstValue, secondValue))

            elif selectedNumber == 4:
                firstValue = int(input("Enter the first value: \n"))
                secondValue = int(input("Enter the second value: \n"))
                print("The result of the Operation is: ", divide(firstValue, secondValue))

            elif selectedNumber == 5:
                firstValue = int(input("Enter the value of the base: \n"))
                secondValue = int(input("Enter the value of the exponent: \n"))
                print("The result of the Operation is: ", power(firstValue, secondValue))

            elif selectedNumber == 6:
                print(byeText.renderText("Bye :)"))
                break

            else:
                print("Invalid type of operation!")


        elif insertedNumber == 2:
            print(byeText.renderText("Bye :)"))
            break
        else:
            print("Option does not exist, please try again!")


    except ValueError:
        print("Only numbers are allowed!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except Exception:
        print("Unspecified error!")
