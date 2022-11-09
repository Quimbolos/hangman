# %% 

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
# %%
# %%
