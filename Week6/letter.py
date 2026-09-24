def main():
  receiver = ["Mario","Luigi","Daisy","Yoshi","Toad","Princess Peach","Bowser"]

  for letter in receiver:
    if letter != ("Princes Peach"):
      print(f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {letter},

       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {receiver[5]}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
""")


if __name__=="__main__":
  main()
