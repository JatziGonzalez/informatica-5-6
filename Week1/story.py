def main():
    name = input("What is your name? ").strip().title()
    color = input("Tell me a color? ").strip().title()
    adjective = input("Give me an adjectice? ").strip().title()
    goal = input("A goal you would like to archive? ").strip().title()

    print(f"Hello ,{name}!")
    print(f"This is your story")
    print(f"In the morning with {color}, and the air felt {adjective}. This is the day I {goal}")

    print("---Yelling Version---")
    print(f"IN THE MORNING {color.upper()}, AND THE AIR FELT {adjective.upper()}. THIS IS THE DAY {goal.upper()}")
main()
