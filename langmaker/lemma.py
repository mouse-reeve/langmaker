''' System for generating lemmas, buildin on existing linguistic data '''
from langmaker.morphology import Morphology

class Lemma(object):
    ''' works with words - produces dictionaries, maybe '''

    def __init__(self, morphology=None):
        self.morphology = morphology or Morphology()

    def get_lemma(self):
        ''' create a lemma '''
        return self.morphology.generate_word()

if __name__ == '__main__':
    builder = Lemma()
    for _ in range(10):
        print(builder.get_lemma())
