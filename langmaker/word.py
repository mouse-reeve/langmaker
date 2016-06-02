''' System for generating words, buildin on existing linguistic data '''
import random

from langmaker.morpheme import Morpheme

class Word(object):
    ''' the dumbest to generate a word - just random letters '''

    def __init__(self, morphemes=None):
        self.morphemes = morphemes or Morpheme()

    def get_word(self):
        ''' create a word '''
        # TODO: intelligently join morphemes
        length = random.choice([1, 1, 1, 2, 2, 3])
        return ''.join([self.morphemes.get_morpheme() for _ in range(length)])

if __name__ == '__main__':
    wordbuilder = Word()
    print(wordbuilder.get_word())
