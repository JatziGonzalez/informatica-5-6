def main():

    valid_nums = []
    for i in range(1,11):

        valid_nums.append(str(i))


    while True:
        print("Welcome to the Time Tables Quiz")
        times_table = (input("Enter the time tables you would like to be tested: ")).lower().strip()
        if times_table == "exit":
            break

        elif times_table in valid_nums:
            max_value = int(input("Enter maximum value for the times table: "))

            print(f"You will be tested for the {times_table} time table")

            for x in range (1, max_value +1):
                answer = x * int(times_table)
                #print(f"{x} times {times_table} is {answer}")
                user_answer = int(input(f"{times_table}x{x}="))
                if user_answer == answer:
                    print("Correct")
                else:
                    print("Incorrect")

            if max_value == max_value:
                print("You are finished")


                break



        else:
            print("Invalid command.")


if __name__=="__main__":
  main()
