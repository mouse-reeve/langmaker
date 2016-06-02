''' Generate linguistically consistent morphemes '''
from numpy.random import choice
from langmaker.syllable import Syllable

class Morpheme(object):
    ''' combine syllables into morphemes '''

    def __init__(self, syllables=None):
        self.syllables = syllables or Syllable()

    def get_morpheme(self, length=None):
        ''' create a morpheme '''
        # TODO: intelligently join syllables
        # TODO: consider free vs bound morphemes
        length = length or choice([1, 2, 3], 1, p=[0.5, 0.49, 0.01])[0]
        return '/'.join([self.syllables.get_syllable() for _ in range(length)])

if __name__ == '__main__':
    builder = Morpheme()
    print(builder.get_morpheme())
