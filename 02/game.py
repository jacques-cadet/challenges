#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from itertools import permutations
import random

from data import DICTIONARY, LETTER_SCORES, POUCH


NUM_LETTERS = 7


def draw_letters():
    """Pick NUM_LETTERS letters randomly. Hint: use stdlib random"""

    return [random.choice(POUCH) for _ in range(NUM_LETTERS)]


def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""
    
    word = input('Please form a word from drawn letters. >> ')
    uppercase = word.upper()
    _validation(uppercase, draw, DICTIONARY)

    return uppercase


def _validation(word, draw, collection=None):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""

    def error(e):
        raise ValueError(e)

    void = ''
    for letter in word:
        if letter not in draw:
            void += letter
        try:
            assert word.count(letter) <= draw.count(letter)
        except AssertionError:
            e = "Too many {}'s in your word".format(letter)
            error(e)

    if void:
        e = '"{}" not in drawn letters, {}'.format(void, draw) 
        error(e)

    if word == ''.join( letter for letter in draw):
        e = 'You have to create a word'
        error(e)

    if collection and word not in DICTIONARY:
        e = 'The word "{}" is not in this dictonary'.format(word)
        error(e)


def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""

    return sum(LETTER_SCORES[char] for char in word.upper()
                if char in LETTER_SCORES)


def max_word_value(words):
    """Calc the max value of a collection of words"""

    return max(words, key=calc_word_value)


class Words:
    """A class for calculating all possible words from a random
    list of characters and a reference list of words """

    def __init__(self, draw, dictionary=DICTIONARY):
        self._draw = draw
        self.dictionary = dictionary

    def __repr__(self):
        return '(<draw="{}">)'.format(self.draw)

    @property
    def draw(self):
        return self._draw

    @staticmethod
    def _get_permutations_draw(draw):
        """Helper for get_possible_dict_words to 
        get all permutations of draw letters.
        Hint: use itertools.permutations"""

        return [n for _ in range(1, len(draw)+1) 
                for n in permutations(draw, _)]

    def get_possible_dict_words(self):
        """Get all possible words from draw which are valid dictionary words.
        Use the _get_permutations_draw helper and DICTIONARY constant"""

        possible = self._get_permutations_draw(self.draw)
        words = [''.join( i for i in a) for a in possible]
        valid_words = set([word for word in words if word in self.dictionary])

        return valid_words


def main():
    """Main game interface calling the previously defined methods"""

    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'
    .format(word.capitalize(), word_score))

    instance = Words(draw)
    possible_words = instance.get_possible_dict_words()
    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    game_score = word_score / max_word_score * 100

    print('Optimal word possible: {} (value: {})'.format(
        max_word.capitalize(), max_word_score))
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
    main()
