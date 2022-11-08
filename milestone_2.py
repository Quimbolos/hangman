# %% 

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


# %%
