def main():

  while True:
    number = int(input("Enter a number: "))
    if number == "exit":
      break

    else:
      for x in range (1,11):
        answer = x * number
        print(f"{x} times {number} is {answer}")
      

if __name__=="__main__":
  main()
