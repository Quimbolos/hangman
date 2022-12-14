# Hangman

> AiCore starting project to introduce Python and Git skills - end goal: create a Hangman game.

## Milestone 1: Set up the environment

Create a new GitHub repo to upload the code and allow version control throughout the project.


## Milestone 2: Create the variables for the Game

Create the variables for the hangman using basic python commands. For each TASK, changes in the code are committed and pushed to the GitHub repo.

```python

import random 

guess = input("Enter your guess: ") # TASK 3

### TASK 4

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')

else:
    print('Oops! That is not a valid input.')

###

word_list = ['watermelon', 'apple', 'strawberries', 'blueberries', 'grapes']
# print(word_list) - TASK 1

word = random.choice(word_list)
# print(world) - TASK 2
```

## Milestone 3: Check if the guessed character is in the word

Check if the guessed letter is in the randomly chosen word. Two functions are defined, one to check if the guess is in the chosen word and another to check if the guess input is valid. Again, changes in the code are committed and pushed to the GitHub repo for each TASK.

```python

import random

word_list = ['watermelon', 'apple', 'strawberries', 'blueberries', 'grapes']

word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess!", guess ,"is in the word")
    else:
        print("Sorry,", guess ,"is not in this word")

def ask_for_input():
    while True:
        guess = input("Enter your guess: ") 
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()

```

## Milestone 4: Create the Game Class

Create a Hangman Class through Object Oriented Programming. A hangman class is created, and its attributes are initialised. After that, methods are created to run checks and define what happens when the letter/guess is in the word and when the letter/guess is not in the word. Again, changes in the code are committed and pushed to the GitHub repo for each TASK.

```python

import random

class Hangman():

    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess!", guess ,"is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = self.word[i]
            self.num_letters = self.num_letters - 1
        else:
            print("Sorry,", guess ,"is not in the word.")
            self.num_lives = self.num_lives - 1
            print("You have", self.num_lives ,"lives left.")


    def ask_for_input(self):
        while True:
            guess = input("Enter your guess: ") 
            if len(guess) != 1 and guess.isalpha() == False:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

word_list_ = ['watermelon', 'apple', 'strawberries', 'blueberries', 'grapes']
my_hangman = Hangman(word_list_,5)
Hangman.ask_for_input(my_hangman)

```

## Milestone 5: Putting it all together

Create a function that takes the word_list as an argument. Within the function, create an instance (game) of the previously created Hangman class. In addition, a while loop is created to continuously ask the user for input until he wins or loses the hangman game. Again, changes in the code are committed and pushed to the GitHub repo for each TASK.

```python

import random

class Hangman():
    
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess!", guess ,"is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = self.word[i]
            self.num_letters = self.num_letters - 1

        else:
            print("Sorry,", guess ,"is not in this word.")
            self.num_lives = self.num_lives - 1
            print("You have", self.num_lives ,"lives left.")


    def ask_for_input(self):
        while True:
            guess = input("Enter your guess: ") 
            if len(guess) != 1 and guess.isalpha() == False:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


def play_game(word_list):
    game = Hangman(word_list, num_lives = 5)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
            print(game.word_guessed)
        elif game.num_lives != 0 and game.num_letters == 0:
            print('Congratulations. You won the game!')
            break

word_list = ['watermelon', 'apple', 'strawberries', 'blueberries', 'grapes']

play_game(word_list)

```