from data import DICTIONARY, LETTER_SCORES


def load_words(file=DICTIONARY):
    """Load dictionary into a list and return list"""

    with open(file, 'r') as dictionary:
        return [word.strip('\n') for word in dictionary]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    return sum(LETTER_SCORES[char] for char in word.upper()
                    if char in LETTER_SCORES)


def max_word_value(words=0):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if not words:
        words = load_words()
    return max(words, key=calc_word_value)


if __name__ == "__main__":

    import unittest
    import test_wordvalue

    test = unittest.TestLoader().loadTestsFromModule(test_wordvalue)
    unittest.TextTestRunner(verbosity=2).run(test)
