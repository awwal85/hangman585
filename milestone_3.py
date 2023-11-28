import random
while True:
    guess = input("Hello!, please guess a letter: ")
    if guess.isalpha():
        break
    else:
        print('Invalid letter. Please, enter a single alphabetical character.')

word_list = ['apple', 'date', 'banana', 'avocado', 'watermelon']
word = random.choice(word_list)
while guess.isalpha():
    if guess in word:
        f'Good guess! {guess} is in the word.'
    else:
        f'Sorry, {guess} is not in the word. Try again'