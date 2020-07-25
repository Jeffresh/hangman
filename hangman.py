# Objectives
#
# The player starts the game with 8 "lives", that is our player can input the wrong letter 8 times.
#
#     Print No such letter in the word and reduce the attempts count if the word guessed by
#     the program doesn't contain this letter.
#     Print No improvements and reduce the attempts count if the guessed word contains this
#     letter but the user tried this letter before.
#     The attempts count should be decreased only if there are no letters to uncover.
#
# Please, make sure that your program's output formatting precisely follows the example output
# formatting. Pay attention to the empty lines between tries and in the end.


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
            tries = 0
            match_word = '-' * len(self.guess_word)
            letters_tried = set()
            while tries < 8 and '-' in match_word:
                print()
                print(match_word)
                letter = input('Input a letter')
                print()

                if letter in letters_tried:
                    tries += 1
                    print('No improvements')

                elif self.guess_word.find(letter) != -1:
                    letters_tried.add(letter)
                    for i in range(len(self.guess_word)):
                        if self.guess_word[i] == letter:
                            match_word = match_word[:i] + letter + match_word[i + 1:]
                else:
                    print('No such letter in the word')
                    tries += 1

            if '-' in match_word:
                print('You are hanged!')
            else:
                print('You guessed the word!', "You survived!", sep='\n')

        else:
            print('You have to add words before start a game.')


if __name__ == '__main__':
    my_game = Hangman()
    my_game.start_game()
