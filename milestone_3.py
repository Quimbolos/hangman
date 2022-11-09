# %% 

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
    while True:
        guess = input("Enter your guess: ") 
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

ask_for_input()



# %%
