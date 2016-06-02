''' System for generating lemmas, buildin on existing linguistic data '''
from numpy.random import choice
from langmaker.morpheme import Morpheme

class Lemma(object):
    ''' the dumbest to generate a lemma - just random letters '''

    def __init__(self, morphemes=None):
        self.morphemes = morphemes or Morpheme()

    def get_lemma(self):
        ''' create a lemma '''
        # TODO: intelligently join morphemes
        length = choice([1, 2], 1, p=[0.9, 0.1])[0]
        return '/'.join([self.morphemes.get_morpheme() for _ in range(length)])

if __name__ == '__main__':
    builder = Lemma()
    for _ in range(10):
        print(builder.get_lemma())
