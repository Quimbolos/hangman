# Hangman

> AiCore start project to introduce Python and Git skills - endgoal: create a Hangman game.

## Milestone 1: Set up the environment

Create a new GitHub repo to upload the code and allow version control throught the project.


## Milestone 2: Create the variables for the Game

Create the variables for the hangman using basic python commands. For each TASK, changes in the code are commited and pushed to the GitHub repo.

```python
"""
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
# print(world) - TASK 2"""
```

## Milestone 3: Check if the guessed character is in the word

Check if the guessed letter is in the randomly chosen word. Two functions are defined, one to check if the guess is in the chosen word, and another one to check if the guess input is valid. Again, for each TASK, changes in the code are commited and pushed to the GitHub repo.

```python
"""
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