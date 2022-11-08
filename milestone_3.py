# %% 
import random
import string 


def check_guess(guess):

    guess = guess.lower()

    if guess in word:
        print("Good guess!", guess,"is in the word")
    
    else:
        print("Sorry,", guess,"is not in this word")


def ask_for_input():

    guess = input("Enter your guess: ") 

    while len(guess) == 1 and guess in alphabet:
        break

    else:
        print('Invalid letter. Please, enter a single alphabetical character.')
  
    check_guess(guess)



alphabet = list(string.ascii_lowercase)

word_list = ['watermelon', 'apple', 'strawberries', 'blueberries', 'grapes']

word = random.choice(word_list)

ask_for_input()



# %%
