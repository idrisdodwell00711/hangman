import random

word_list = ['pomme cannel', 'lychee', 'anannas', 'pomme','citron']

word = random.choice(word_list)

print(word)

guess = input()

if(len(guess)==1 and type(guess) == str):
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')