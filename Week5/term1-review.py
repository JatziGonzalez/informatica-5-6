from datetime import datetime
def main():

    day = datetime.now().weekday()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(day)

    if day <= 4:
        print("Its a weekday")
        remaining = 5 - day
        print(remaining, "days until the weekend")
    elif day == 4:
        print("It's Friday")
        print("Just a day left until the weekend")

    months = ["January", "February"; "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print("These are the summer months:")
    print(months[])
    print(months[])
    print(months[])

    seasons = ["Winter", "Spring", "Sumer", "Autumn"]

    print("What month is it? (1-12)")
    month = int(input())

    if month <= 2 or month == 12:
        season = 0
    elif month <= 5:
        season = 1
    elif month <= 8:
        season = 2
    else:
        season = 3
    print("It is", seasons[season])


    else:
    print("Its the weekend")
if __name__=="__main__":
    main()
