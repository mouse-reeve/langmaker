''' Generate linguistically consistent morphemes '''
from numpy.random import choice
from langmaker.syllable import Syllable

class Morpheme(object):
    ''' combine syllables into morphemes '''
    # TODO: this may not be a necessary class
    affixes = {}

    def __init__(self, syllables=None):
        self.syllables = syllables or Syllable()

    def get_morpheme(self, length=None):
        ''' create a morpheme '''
        # TODO: intelligently join syllables
        # TODO: consider free vs bound morphemes
        length = length or choice([1, 2, 3], 1, p=[0.5, 0.49, 0.01])[0]
        return '/'.join([self.syllables.get_syllable() for _ in range(length)])

    def get_affix(self, tag):
        if not tag in self.affixes:
            self.affixes[tag] = self.get_morpheme(length=1)
        return self.affixes[tag]

if __name__ == '__main__':
    builder = Morpheme()
    print(builder.get_morpheme())
