def main():
    spain = input("Spain goals: ")
    argentina = input("Argentina goals: ")

    if spain > argentina:
        print("Spain is the Winner!")
    elif argentina > spain:
        print("Argentina is the Winner!")
    else:
        print("It's a tie.")

    print("gg")

if __name__=="__main__":
    main()
