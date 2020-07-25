# Objectives
#
#     Create the following word list: 'python', 'java', 'kotlin', 'javascript'.
#     Program the game to choose a random word from it. You can enter more words, but let's stick to these four for now.


import random


class Hangman:

    def __init__(self):
        self.words = ['python', 'java', 'kotlin', 'javascript']
        self.guess_word = ''

    def add_words(self, word):
        self.words.append(word)

    def start_game(self):
        if self.words:
            self.guess_word = random.choice(self.words)
            print('H A N G M A N')
            guess = input('Guess the word:')
            if guess == self.guess_word:
                print('You survived!')
            else:
                print('You are hanged!')
        else:
            print('You have to add words before start a game.')


if __name__ == '__main__':
    my_game = Hangman()
    my_game.start_game()
