# Objectives
#
#     If the user enters the same letter twice then the program should output You already typed
#     this letter .
#     Also, you should check if the user prints an English lowercase letter or not. If not,
#     the program should print It is not an ASCII lowercase letter .
#     Also, you should check if the user printed exactly one letter. If not, the program
#     should print You should input a single letter . Remember that zero is also not one!
#     Note that all these three errors should not reduce attempts count!
#
# Please, make sure that your program's output formatting precisely follows the example output
# formatting. Pay attention to the empty lines between tries and in the end.
#
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
                letter = input('Input a letter:')

                if len(letter) > 1 or len(letter) < 1:
                    print('You should input a single letter')

                elif letter in letters_tried:
                    print('You already typed this letter')
                elif not letter.isalpha() or letter.isupper():
                    print('It is not an ASCII lowercase letter')

                elif self.guess_word.find(letter) != -1:
                    for i in range(len(self.guess_word)):
                        if self.guess_word[i] == letter:
                            match_word = match_word[:i] + letter + match_word[i + 1:]
                else:
                    print('No such letter in the word')
                    tries += 1
                letters_tried.add(letter)

            if '-' in match_word:
                print('You are hanged!')
            else:
                print('You guessed the word!', "You survived!", sep='\n')

        else:
            print('You have to add words before start a game.')


if __name__ == '__main__':
    my_game = Hangman()
    my_game.start_game()
