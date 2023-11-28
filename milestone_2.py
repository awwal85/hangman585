import random
word_list = ['apple', 'date', 'banana', 'avocado', 'watermelon']
print(word_list)
word = random.choice(word_list)
print(word)
guess = input('Hello!, please enter a single letter: ')
if guess.isalpha() and len(guess) == 1:
    print('Good guess!')
else:
    print('Oops! That is not a valid input')