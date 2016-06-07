''' System for generating lexemes, lemmas, and words, buildin on existing linguistic data '''
from langmaker.morphology import Morphology

class Lexeme(object):
    ''' works with words '''

    def __init__(self, morphology=None):
        self.morphology = morphology or Morphology()

    def get_lemma(self):
        ''' get the dictionary form of a lexeme '''
        return self.morphology.generate_lemma()
        return self.get_word()

    def get_lexeme_set(self):
        ''' produce the words for a lexeme (ie: ['run', 'ran']) '''
        # TODO: actually produce the set of words for a lexeme
        return [self.get_word()]

    def get_word(self):
        ''' create a word (lemma or lexeme) '''
        # TODO: do some actual morphology
        return self.get_lemma()

if __name__ == '__main__':
    builder = Lexeme()
    for _ in range(10):
        print(builder.get_lexeme())
