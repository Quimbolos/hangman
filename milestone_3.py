# %% 
import random
import string 


guess = input("Enter your guess: ") 

alphabet = list(string.ascii_lowercase)

while len(guess) == 1 and guess in alphabet:

    break

else:
    print('Invalid letter. Please, enter a single alphabetical character.')



word_list = ['watermelon', 'apple', 'strawberries', 'blueberries', 'grapes']
# print(word_list) 

world = random.choice(word_list)
# print(world) 

# %%
