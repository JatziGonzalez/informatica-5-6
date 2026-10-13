# Define the main function
# Have a txt file with random words
# Get the number of letters that the word
# Print a underscore for each letter
# Give the user 10 opportunities
# If the user messes up -= opportunities
# If the user guesses correctly keep the current score
# Keep repeating the loop until the user guesses the
#
#
#
#
#
#
#
#
#
#
#
#
import random
def main():

    word("randomwords.txt")
def word(file):
    with open(file) as word_file:
        content = word_file.read().splitlines()
        print(random.choice(content))




if __name__=="__main__":
    main()
