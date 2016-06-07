''' System for generating lexemes, lemmas, and words, buildin on existing linguistic data '''
from langmaker.morphology import Morphology

class Lexeme(object):
    ''' works with words - produces dictionaries, maybe '''

    def __init__(self, morphology=None):
        self.morphology = morphology or Morphology()

    def get_word(self):
        ''' create a word (lemma or lexeme) '''
        return self.morphology.generate_word()

if __name__ == '__main__':
    builder = Lexeme()
    for _ in range(10):
        print(builder.get_lexeme())
