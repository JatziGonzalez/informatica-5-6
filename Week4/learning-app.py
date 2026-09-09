import random
def main():

    print("Get SmarTer")
    streak = 0

    while streak < 3:

        number1 = random.randint(10,99)
        number2 = random.randint(10,99)
        result = int((number1 + number2))
        response = int((input(f"{number1}+{number2}=")))


        if response == result:
            print("Correct Result")
            streak += 1
            print("Streak ⭐")
        else:
            print("Try again")
            print ("The answer was", result)

            streak = 0
            print("")

    print("You got 3 correct ⭐⭐⭐")


if __name__ =="__main__":
    main()
