''' Generate linguistically consistent morphemes '''
import random

from langmaker.syllable import Syllable

class Morpheme(object):
    ''' combine syllables into morphemes '''

    def __init__(self, syllables=None):
        self.syllables = syllables or Syllable()

    def get_morpheme(self, length=None):
        ''' create a morpheme '''
        # TODO: intelligently join syllables
        # TODO: consider free vs bound morphemes
        length = length or random.choice([1, 2, 2, 2, 3])
        return '/'.join([self.syllables.get_syllable() for _ in range(length)])

if __name__ == '__main__':
    builder = Morpheme()
    print(builder.get_morpheme())
