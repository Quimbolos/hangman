# %%
import random
class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.world_guessed = ['_']*len(self.word)
        self.num_letters = self.world_guessed.count('_')
        self.list_of_guesses = []
        

# %%
