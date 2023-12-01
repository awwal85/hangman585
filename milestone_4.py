import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives

    def check_guess(guess):
        list_letters = []
        guess = guess.lower()
        word_list = ['apple', 'date', 'banana', 'avocado', 'watermelon']
        word = random.choice(word_list)
        word_guessed = print(['-'*len(word)])
        for i, letter in enumerate(word_guessed):
            if letter != '-' and guess == letter:
                word[i] = letter
                print(''.join(word))
            else:
                num_lives -= 1
                f'Sorry, {letter} is not in the word.'
                f'You have {num_lives} lives left.'

    def ask_for_input(self):
        list_of_guesses = []
        while True:
            guess = input("Hello!, please guess a letter: ")
            
            if guess.isnotalpha() and len(guess) != 1:
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                list_of_guesses = list_of_guesses.append(guess)
    ask_for_input()