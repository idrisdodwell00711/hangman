import random

class Hangman:
    def  __init__(self, word_list, num_lives=5):
        self.word_list = word_list,
        self.num_lives = num_lives
        self.ran_num = random.randint(0, len(word_list)-1)
        self.word = self.word_list[0][self.ran_num]
        self.word_guess = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guess =[]
        
    def check_guess(self,guess):
        self.lc_guess = guess.lower()
        print(self.lc_guess, self.word)
        if(self.lc_guess in self.word):
            print(f'Good guess! {guess} is in the word.')
            for _ in self.word_guess:
               print(self.word.index(self.lc_guess))
               inx = self.word.index(self.lc_guess)
               self.word_guess[inx] = self.lc_guess
            self.num_letters = self.num_letters-1
            print(self.num_letters)
        else:
            self.num_lives = self.num_lives -1
            print(f'Sorry, {guess} is not in the word. Try again')
            print(f'You have {self.num_lives} lives left.')
        
    def ask_forInput(self):
        self.guess = input()
        while True:
            if(not self.guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')
                break
            elif(self.guess in self.list_of_guess):
                print("You already tried that letter!")
                break   
            else:
                self.check_guess(self.guess)
                self.list_of_guess.append(self.guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    
    while True:
        if(game.num_lives==0):
            print('You have lost')
            break
        elif(game.num_letters>0):
            game.ask_forInput()
        elif(game.num_lives>0 and not game.num_letters>0):
            print(game.num_lives, game.num_letters)
            print('Congrats, you won!')
            break
            
play_game(['hardy', 'hxuhsuxbu'])
    