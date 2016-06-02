''' System for generating words, buildin on existing linguistic data '''
from numpy.random import choice
from langmaker.morpheme import Morpheme

class Word(object):
    ''' the dumbest to generate a word - just random letters '''

    def __init__(self, morphemes=None):
        self.morphemes = morphemes or Morpheme()

    def get_word(self):
        ''' create a word '''
        # TODO: intelligently join morphemes
        length = choice([1, 2], 1, p=[0.9, 0.1])[0]
        return '/'.join([self.morphemes.get_morpheme() for _ in range(length)])

if __name__ == '__main__':
    wordbuilder = Word()
    for _ in range(10):
        print(wordbuilder.get_word())
