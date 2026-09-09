import random
def main():

    guess = int(input("If you guess TAILS enter 1, If you guess HEADS enter 2: "))

    number = random.randint(1,2)

    if number == 1:
        print ("Tails")
    else:
        print("Heads")
 #_________________________

    if guess == number:
        print ("Winner")
    else:
        print ("Loser")






if __name__ =="__main__":
    main()
