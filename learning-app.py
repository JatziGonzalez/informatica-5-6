import random
def main():

    print("Get SmarTer")

    number1 = random.randint(10,99)
    number2 = random.randint(10,99)
    result = int((number1 + number2))
 

    response = int((input(f"{number1}+{number2}=")))


    while response < 3:
        print("")

    if response == result:
        print("Correct Result ⭐")
        response += 1
    else:
        print("Try again")










if __name__ =="__main__":
    main()
