guess = input()
word = 'apple'
    
def check_guess(guess): 
    lower_guess = guess.lower()
    
    if(lower_guess in word):
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again')
            
def ask_forInput():
    while True:
        if(guess.isalpha()):
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
            break
    check_guess(guess)

ask_forInput()