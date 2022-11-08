# %% 
import random
import string 


guess = input("Enter your guess: ") 

alphabet = list(string.ascii_lowercase)

### TASK 1

while len(guess) == 1 and guess in alphabet:

    break

else:
    print('Invalid letter. Please, enter a single alphabetical character.')

###

word_list = ['watermelon', 'apple', 'strawberries', 'blueberries', 'grapes']
# print(word_list) 

world = random.choice(word_list)
# print(world) 

### TASK 2

if guess in world:
    print("Good guess!", guess,"is in the word")
    
else:
    print("Sorry,", guess,"is not in this word")

###

# %%
