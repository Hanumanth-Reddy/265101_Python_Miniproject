import sys
import random

name = input("UserName: ")
welcome = "Hello, \"{n}\"".format(n=name)
print(welcome)


def menu():
    print("--------------MENU---------------")
    print("1: PLAYER")
    print("2: ADMIN")
    print("3: EXIT")
    option = int(input('Enter option: '))
    if option == 1:
        play()
    elif option == 2:
        admin()
    elif option == 3:
        print("Thank You")
        sys.exit()


def admin():
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
        print("Admin LOGOUT")
        menu()


def add():
    new_word = input("Enter word to Add: ")
    with open('words.txt', "a") as file:
        file.write(new_word + "\n")
        print("Successfully added")
    more = input("Want to add more words y/n: ")
    if more == 'y':
        add()
    elif more == 'n':
        print("Added")
        admin()
    else:
        print('wrong input')


def view():
    sub = []
    with open("words.txt", "r") as file:
        wordlist = set(file.readlines())
        for i in wordlist:
            sub.append(i.replace("\n", ""))
        print(sub)
    admin()


def play():
    print(f"\"{name}\"  LETS\'S PLAY HANGMAN!")
    print(" You have 8 chances to guess the word\n")
    newest = []
    with open("words.txt", "r") as file:
        wordlist = set(file.readlines())  # using set to take awy duplicates words that are in file more than once.
        for i in wordlist:
            newest.append(i.replace("\n", ""))

    word = random.choice(newest)
    print("The word You have to guess is " + str(len(word)) + " characters long")
    guesses = " "
    turn = 8
    while turn > 0:
        wrong = 0
        for char in word:
            if char in guesses:
                print(char, end="")
            else:
                print(" _ ", end=" ")
                wrong += 1
        if wrong == 0:
            print("\nHURRAY U WON!")
            choice = input("Play Again? y/n\n")
            if "y" in choice:
                play()
            elif "n" in choice:
                sys.exit()
            else:
                print("Wrong Choice, type y or n.")
        guess = input("\tGuess Character: ")
        guesses += guess
        if guess not in word:
            turn -= 1
            print("\nOH NO! ... invalid character, ", end="")
            print(f"You have {turn} chances left.")
            if turn == 0:
                print("You lost Try Again!!")
                choice = input("Play Again? y/n\n")
                if "y" in choice:
                    play()
                elif "n" in choice:
                    menu()
                else:
                    sys.exit()


menu()
