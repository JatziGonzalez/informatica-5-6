import random
def main():
    number = random.randint(1,100)
    guess = int()

    user = input("What is your name?: ")
    print("Okey",user,"I am thinking of a number between 1 and 100.")
    while guess != number:
        guess = int(input("Take a guess: "))
        if guess > number:
            print("To high")
        elif guess < number:
            print("To low")

        elif guess == number:
            print("Good job",user,"You guessed correct my number!")



