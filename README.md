# Hangman

> AiCore start project to introduce Python and Git skills - endgoal: create a Hangman game.

## Milestone 1: Set up the environment

Create a new GitHub repo to upload the code and allow version control throught the project.


## Milestone 2: Create the variables for the Game

Create the variables for the hangman using basic python commands. For each TASK, changes in the code are commited and pushed to the GitHub repo.

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
# print(world) - TASK 2
```

## Milestone 3: Check if the guessed character is in the word

Check if the guessed letter is in the randomly chosen word. Two functions are defined, one to check if the guess is in the chosen word, and another one to check if the guess input is valid. Again, for each TASK, changes in the code are commited and pushed to the GitHub repo.

```python

import random

word_list = ['watermelon', 'apple', 'strawberries', 'blueberries', 'grapes']

word = random.choice(word_list)

def check_guess(guess):

    guess = guess.lower()

    if guess in word:
        print("Good guess!", guess,"is in the word")
    
    else:
        print("Sorry,", guess,"is not in this word")

def ask_for_input():

    guess = input("Enter your guess: ") 

    while len(guess) == 1 and guess.isalpha():
        break

    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
  
    check_guess(guess)

ask_for_input()
```

## Milestone 4: Create the Game Class

Create a Hangman Class through Object Oriented Programming. A hangman class is created and its attributes are inistialised. After that, methods are created to run checks and define what happens when the letter/guess is in the word and when the letter/guess is not in the word. Again, for each TASK, changes in the code are commited and pushed to the GitHub repo.

```python

import random

class Hangman():
    def __init__(self, wordlist, num_lives = 5):
        self.wordlist = wordlist
        self.num_lives = num_lives
        self.word = random.choice(self.wordlist)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(self.word_guessed)
        self.list_of_guesses = ['']

    def check_guess(self, guess):

        guess = guess.lower()

        if guess in self.word:
            print("Good guess!", guess,"is in the word")
            n_guess = 0
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    n_guess = n_guess + 1
                    self.word_guessed[i] = self.word[i]
            self.num_letters = self.num_letters - n_guess

        else:
            print("Sorry,", guess,"is not in this word")
            self.num_lives = self.num_lives - 1
            print("You have", self.num_lives,"lives left")

        self.list_of_guesses.append(guess)

    def ask_for_input(self):

        guess = input("Enter your guess: ") 

        while len(guess) == 1 and guess.isalpha():
            break

        if len(guess) != 1 and guess.isalpha() == False:
            print('Invalid letter. Please, enter a single alphabetical character.')
        
        elif guess in self.list_of_guesses:
            print('You already tried that letter!')

        else:
            self.check_guess(guess)

word_list = ['watermelon', 'apple', 'strawberries', 'blueberries', 'grapes']
my_hangman = Hangman(word_list,5)
Hangman.ask_for_input(my_hangman) 
```

## Milestone 5: Putting it all together

Create a function that takes the word_list as an argument. Within the function create an instance (game) of the previously created Hangman class. In addition, as while loop is created to continously ask the user for input until he wins or loses the hangmane game. Again, for each TASK, changes in the code are commited and pushed to the GitHub repo.

```python

import random

class Hangman():
    def __init__(self, wordlist, num_lives = 5):
        self.wordlist = wordlist
        self.num_lives = num_lives
        self.word = random.choice(self.wordlist)
        self.word_guessed = ['_']*len(self.word)
        self.num_letters = len(self.word_guessed)
        self.list_of_guesses = ['']

    def check_guess(self, guess):

        guess = guess.lower()

        if guess in self.word:
            print("Good guess!", guess,"is in the word")
            n_guess = 0
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    n_guess = n_guess + 1
                    self.word_guessed[i] = self.word[i]
            self.num_letters = self.num_letters - n_guess

        else:
            print("Sorry,", guess,"is not in this word")
            self.num_lives = self.num_lives - 1
            print("You have", self.num_lives,"lives left")

        self.list_of_guesses.append(guess)

    def ask_for_input(self):

        guess = input("Enter your guess: ") 

        while len(guess) == 1 and guess.isalpha():
            break

        if len(guess) != 1 and guess.isalpha() == False:
            print('Invalid letter. Please, enter a single alphabetical character.')
        
        elif guess in self.list_of_guesses:
            print('You already tried that letter!')

        else:
            self.check_guess(guess)


def play_game(wordlist):
    game = Hangman(wordlist, num_lives = 5)
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