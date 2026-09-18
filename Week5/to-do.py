from os import remove
def main():
  tasks = []

  while True:
    print(f"Task to do: {len(tasks)}")
    print(tasks)

    command = input("What do you want to do? (add, complete, exit): ")
    if command == "add":
      new_task = input("Enter new task: ")
      tasks.append(new_task)
    elif command == "complete":
      to_do = input("Which one did you complete: ")
      tasks.remove(to_do)
    elif command == "exit":
      print("You are done!!")
      break



if __name__ =="__main__":
  main()