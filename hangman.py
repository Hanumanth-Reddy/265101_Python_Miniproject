import sys
import random
from time import sleep
<<<<<<< HEAD

=======
>>>>>>> origin/master
# Hangman game with Words from file.
# No of spaces are fetched dynamically according to word length.
# features: admin and player.
# used modules time,sys,random.

name = input("UserName: ")
WELCOME = "Hello, \"{n}\"".format(n=name)
print(WELCOME)


def menu():
    """Menu of game contains play and admin options"""
    print("--------------  MENU  ---------------")
    print("1: PLAYER")
    print("2: ADMIN")
    print("3: EXIT")
    option = int(input('Enter option: '))
    if option == 1:
        sleep(1)
        play()
    elif option == 2:
        sleep(1)
        admin()
    elif option == 3:
        sleep(1)
        print("Thank You!!")
        sys.exit()


def admin():
    """ contains all the admin controls like adding words and viewing words that are used in game"""
    print("\t *** WELCOME ADMIN ***\t")
    print("MANAGE THE WORDS IN GAME")
    print("1: Add")
    print("2: View Words")
    print("3: MENU")
    choice = int(input('Enter your choice: '))
    if choice == 1:
        add()
    elif choice == 2:
        view()
    elif choice == 3:
        print("Admin --> LOGOUT")
        menu()


def add():
    """
    appending new word to words.txt file in a new line everytime
    and using with for opening file so that file closes automatically
    """
    new_word = input("Enter word to Add: ")
<<<<<<< HEAD
    new_word = new_word.lower()  # case conversion to avoid conflicts while play game
    print(new_word)
=======
>>>>>>> origin/master
    with open('words.txt', "a") as file:
        file.write(new_word + "\n")
        sleep(1)
        print("Successfully added")
    more = input("Want to add more words y/n: ")
    if more == 'y':
        add()
    elif more == 'n':
        sleep(1)
        print("Added")
        admin()
    else:
        print('wrong input')


def view():
    """reading contents of words.txt file and using with for opening file
    so that file closes automatically
    """
    sub = []
    with open("words.txt", "r") as file:
        wordlist = set(file.readlines())
        for i in wordlist:
            sub.append(i.replace("\n", ""))
        print(sub)
    admin()


def play():
    """
    play game every time it chooses a random word from words.txt file.
    spaces will be generated according to the length of word.
    total of 10 chances are given to guess the correct word.
    used set while reading file data with read lines to take away duplicate word.
    used string formatting. and sleep to provide some delay between function working.
    """
    print(f"\"{name}\"  LETS\'S PLAY HANGMAN!")
<<<<<<< HEAD
    print(" You have 8 chances to guess the word\n")
=======
    print(" You have 10 chances to guess the word\n")
>>>>>>> origin/master
    newest = []
    with open("words.txt", "r") as file:
        # using set to take awy duplicates words that are in file more than once.
        wordlist = set(file.readlines())
        for i in wordlist:
<<<<<<< HEAD
            newest.append(i.replace("\n", ""))  # appending items of wordlist to newest list
=======
            newest.append(i.replace("\n", ""))   # appending items of wordlist to newest list
>>>>>>> origin/master

    word = random.choice(newest)
    print("The word You have to guess is " + str(len(word)) + " characters long")
    guesses = " "
<<<<<<< HEAD
    turn = 8  # number of chances given to guess the word.
=======
    turn = 10     # number of chances given to guess the word.
>>>>>>> origin/master
    while turn > 0:
        wrong = 0
        for char in word:
            if char in guesses:
                print(char, end="")
            else:
                print(" _ ", end=" ")
                wrong += 1
        if wrong == 0:
            sleep(1)
<<<<<<< HEAD
            print("\nYAY You Are Saved!")
            try_again()
        guess = input("\tGuess Character: ")[0]  # reads only 1st character from input
        guess = guess.lower()
        guesses += guess
        if guess not in word:
            turn -= 1
            print("\nOH NO! ... invalid character, ", end="")
            print(f"You have {turn} chances left.")  # shows number of turns remaining
            if turn == 0:
                print("You are HANGED!!")
                try_again()


def try_again():
    """
    to ask user whether to play again or end game
    """
    choice = input("Play Again? y/n\n")
    if "y" in choice:
        play()
    elif "n" in choice:
        print("Game Ended ---> Thank You!")
        sys.exit()
    else:
        print("ERROR: Wrong Choice")
        sys.exit()
=======
            print("\nYAY YOUR Saved!")
            choice = input("Play Again? y/n\n")
            if "y" in choice:
                play()
            elif "n" in choice:
                print("THANK YOU FOR PLAYING")
                sys.exit()
            else:
                print("ERROR: Wrong Choice")
                sys.exit()
        guess = input("\tGuess Character: ")[0]  # reads only 1st character from input
        if guess not in word:
            turn -= 1
            print("\nOH NO! ... invalid character, ", end="")
            print(f"You have {turn} chances left.")     # shows number of turns remaining
            if turn == 0:
                print("You are HANGED!!")
                choice = input("Play Again? y/n\n")
                if "y" in choice:
                    play()
                elif "n" in choice:
                    print("Thank You!")
                    sys.exit()
                else:
                    print("ERROR: Wrong Choice")
                    sys.exit()
>>>>>>> origin/master


menu()
