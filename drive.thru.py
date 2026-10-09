def main():
    print("Welcome to CHESEBURGER")
    welcome()
    menu = ["Cheeseburger", "Fries", "Soda", "IceCream", "Cookie"]
    print(f"Here is the {menu}")



def get_item(meal):
    if meal == 1:
        print("🍔")
    if meal == 2:
        print("🍟")
    if meal == 3:
        print("🥤")
    if meal == 4:
        print("🍦")
    if meal == 5:
        print("🍪")
    else:
        print("Not in our menu, Please order form 1 to 5")


if __name__ == "__main__":
    main()
