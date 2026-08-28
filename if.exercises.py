def main():
    #Absulute Value Calculator
    interger = int(input("Type an integer number: "))
    number = interger * -1

    if interger < 0:
        print(number)
    else:
        print(interger)


    #Interger Calculator
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    operation = input("Enter an operation: ")

    if operation == "add":
        result = first + second
        print(result)
    elif operation == "subtract":
        result = first - second
        print(result)
    elif operation == "multiply":
        result = first * second
        print(result)
    else:
        print()


    #Sting Calculator

    expression = input("Enter an arithmetic expression: ")

    number1, operator, number2 =
    expression.slit()

    number1 = float(number1)
    number2 = float(number2)

    if operator == "+":
        result = number1 + number2
        print(f"{result:.1f}")




if __name__=="__main__":
    main()
