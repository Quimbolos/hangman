# %%
import random
import string
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
            for i in len(self.word):
                if self.word[i] == guess:
                    self.word_guessed[i] = self.word[i]
            self.num_letters = self.num_letters - 1

        else:
            print("Sorry,", guess,"is not in this word")
            self.num_lives = self.num_lives - 1
            print("You have", self.num_lives,"lives left")

        self.list_of_guesses.append(guess)

    def ask_for_input(self):

        guess = input("Enter your guess: ") 

        alphabet = list(string.ascii_lowercase)

        while len(guess) == 1 and guess in alphabet:
            break

        if len(guess) != 1 and guess not in alphabet:
            print('Invalid letter. Please, enter a single alphabetical character.')
        
        elif guess in self.list_of_guesses:
            print('You already tried that letter!')

        else:
            self.check_guess(guess)

word_list = ['watermelon', 'apple', 'strawberries', 'blueberries', 'grapes']
my_hangman = Hangman(word_list,5)
Hangman.ask_for_input(my_hangman)


# %%
