import random
from art import stages, result, logo, lifes
from words import word_list
print(logo,"\nWelcome to HangMan")
x = True
while x == True:
    chosen_word = random.choice(word_list)
    lives = 6

    given_letters = []
    display = []
    # prints _ for letters in a word
    for letter in chosen_word:
        display.append("_")
    print(display)
    i = 0
    print(stages[-1])
    while "_" in display and lives > 0:
        guess = input("Guess a letter: ").lower()
        while guess in given_letters:
            guess = input(f"Guess a letter You have all ready choise {guess}: ").lower()

        given_letters.append(guess)
        i = 0
        position = []
        for letter in chosen_word:

            if letter == guess:
                display.pop(i)
                display.insert(i, guess)

                # print("Right")
                # print(i)
            i += 1
        if not guess in chosen_word:
            lives -= 1
            print(f"Remanig lives {lifes[lives - 1]}\n{stages[lives]}")

        print(display)
    if "-" in display or lives == 0:
        print(result[1], f"\nThe word is {chosen_word}")
    else:
        print(result[0], f"\nThe word is {chosen_word}")
    #print(display)
    user = input("Press 'p' to play again \nPress 'q' to quit\nPress: ")
    if user.lower() == 'q':
        x = False