def main():
    first = input("Make a face: ")

    first = first.replace(":)", "🙂")
    first = first.replace(":(", "🙁")

    print(first)
    main()
