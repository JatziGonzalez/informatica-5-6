def main():
    print("TeQueria")
    rating = float(input("Give us your rating from 0 to 5: "))

    if rating > 4.5:
        print("Perfection")
    elif rating > 4:
        print("Excellent")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("Fair")
    elif rating > 1:
        print("Poor")
    else:
        print("Thanks for your opinion!")

if __name__=="__main__":
    main()
