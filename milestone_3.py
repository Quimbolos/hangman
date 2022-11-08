# %% 

import random

word_list = ['watermelon', 'apple', 'strawberries', 'blueberries', 'grapes']

word = random.choice(word_list)

while True:

    guess = input("Enter your guess: ") 

    guess = guess.lower()

    if len(guess) == 1 and guess.isalpha():
        break

    else:
        print("Invalid letter. Please, enter a single alphabetical character.")



if guess in word:
    print("Good guess!", guess,"is in the word")

else:
    print("Sorry,", guess,"is not in this word")



# %%
