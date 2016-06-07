''' Morphological rules for grammar and word construction '''
from numpy.random import choice
from langmaker.morpheme import Morpheme

class Morphology(object):
    ''' interrelated grammar and word structures '''

    def __init__(self, morphemes=None):
        self.morphemes = morphemes or Morpheme()

    def generate_lemma(self):
        ''' combine morphemes into lemmas '''
        # TODO: intelligently join morphemes
        # TODO: meaningful morpheme count
        length = choice([1, 2], 1, p=[0.9, 0.1])[0]
        return '/'.join([self.morphemes.get_morpheme() for _ in range(length)])

if __name__ == '__main__':
    builder = Morphology()
    for _ in range(10):
        print(builder.generate_lemma())
