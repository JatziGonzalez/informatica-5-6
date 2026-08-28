def main():

    result = input("Descent Atmosphere Layer: ").strip().title()

    if result == "exosphere":
        print("Your altitude level will be between 700 and 10,000 km")
    elif result == "thermosphere":
        print("Your altitude level will be between 85 and 700 km")
    elif result == "mesosphere":
        print("Your altitude level will be between 50 and 85 km")
    elif result == "stratosphere":
        print("Your altitude level will be between 12 and 50 km")
    elif result == "troposphere":
        print("Your altitude level will be between 0 and 12 km")

    altitude = float(input("Enter exact altitud: "))
    time= 0
    if altitude > 700:
        time+= (altitude - 700) / 2
        altitude = 700
    if altitude > 85:
        time+= (altitude - 85) / 0.5
        altitude = 85
    if altitude > 50:
        time+= (altitude - 50) / 0.2
        altitude = 50
    if altitude > 12:
        time+= (altitude - 12) / 0.075
        altitude = 12





if __name__=="__main__":
    main()
