# Hangman With File I/O and Functions

- Static Code Analysis pylint:
      
     [![Static Code Analysis - pylint](https://github.com/Hanumanth-Reddy/265101_Python_Miniproject/actions/workflows/Static%20Code%20analysis%20-%20pylint.yml/badge.svg)](https://github.com/Hanumanth-Reddy/265101_Python_Miniproject/actions/workflows/Static%20Code%20analysis%20-%20pylint.yml)

## Files:

- `hangman.py` - complete project code.
- `words.txt`  - file that contains words to play game, and some operations for 
   admin like read and write data to file.
  
## Functions used:

- `menu()` - Menu to choose admin or player.
  
- `admin()`- Contains admin controls like adding words and viewing file contents.
  
- `play()` - Total game controls are present in here.
  
- `add()`  - Adding Words to `words.txt` file.
  
- `view()` - Read `words.txt` file contents.
  
- `try_again()` - To ask whether user want to play again or exit.

## Working:

- Initially menu() was called and displays operations.
  
- `Admin`- admin can perform read and write to file.
  
- `play` - Every time player start to play game a new words will be picked from file dynamically using random function
  and spaces are provided according to the length of word. player has 8 chances to guess a words to win else lost.
  once the play was ended, it will prompt the player whether they want to play again or end.
  
## Modules imported:

- `sys`    - exit() is used.
  
- `random` - choice() is used to pick random word.
  
- `time`   - sleep() to produce time delay between functions.
