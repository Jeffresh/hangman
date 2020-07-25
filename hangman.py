# Objectives
#
# Now your game should work the following way:
#
#     A player has exactly 8 tries and enters letters. If a player has more tries but he actually
#     guessed the word, it doesn't mean anything.
#     If the letter doesn't occur in the word, the computer takes one try away, even
#     if the user already inputted this letter before.
#     If the player doesn't have any more attempts, the game should end and the program should show a losing message.
#     Otherwise, the player can continue to input letters.
#     Also, use our previous word list: 'python', 'java', 'kotlin', 'javascript' so that your program can be tested
#     more reliably.
#
# Please, make sure that your program's output formatting precisely follows the example output formatting.
# Pay attention to the empty lines between tries and in the end.

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
            print('H A N G M A N\n')
            tries = 0
            match_word = '-' * len(self.guess_word)
            while tries < 8:
                print(match_word)
                letter = input('Input a letter\n')
                if self.guess_word.find(letter) != -1:
                    for i in range(len(self.guess_word)):
                        if self.guess_word[i] == letter:
                            match_word = match_word[:i] + letter + match_word[i + 1:]
                            self.guess_word = self.guess_word[:i] + '_' + self.guess_word[i + 1:]
                else:
                    print('No such letter in the word\n')
                tries += 1
                print()

            print('Thanks for playing!', "We'll see how well you did in the next stage", sep='\n')
        else:
            print('You have to add words before start a game.')


if __name__ == '__main__':
    my_game = Hangman()
    my_game.start_game()
