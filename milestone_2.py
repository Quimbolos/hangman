# %% 
import random
import string # TASK 4


guess = input("Enter your guess: ") # TASK 3

### TASK 4

alphabet = list(string.ascii_lowercase)

if len(guess) == 1 and guess in alphabet:
    print('Good guess!')

else:
    print('Oops! That is not a valid input.')

###

word_list = ['watermelon', 'apple', 'strawberries', 'blueberries', 'grapes']
# print(word_list) - TASK 1

word = random.choice(word_list)
# print(world) - TASK 2


# %%
