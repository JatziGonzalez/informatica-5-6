def main():

    result = input("Descent Atmosphere Layer: ")

    if result == "Exosphere":
        print("Your altitude level will be between 700 and 10,000 km")
    elif result == "exosphere":
        print("Your altitude level will be between 700 and 10,000 km")
    elif result == "Thermosphere":
        print("Your altitude level will be between 85 and 700 km")
    elif result == "thermosphere":
        print("Your altitude level will be between 85 and 700 km")
    elif result == "Mesosphere":
        print("Your altitude level will be between 50 and 85 km")
    elif result == "mesosphere":
        print("Your altitude level will be between 50 and 85 km")
    elif result == "Stratosphere":
        print("Your altitude level will be between 12 and 50 km")
    elif result == "stratosphere":
        print("Your altitude level will be between 12 and 50 km")
    elif result == "Troposphere":
        print("Your altitude level will be between 0 and 12 km")
    else:
        print("Your altitude level will be between 0 and 12 km")

    altitude = float(input("Enter exact altitud: "))

    if altitude < 75:
            print(altitude/"175.0s")
    if altitude < 50:
            print(altitude/"230.0s")
    if altitude < 85:
            print(altitude/"600.0s")
    if altitude < 0:
        print(altitude/"600.0s")


if __name__=="__main__":
    main()
