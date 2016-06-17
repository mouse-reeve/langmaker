''' System for generating lexemes, lemmas, and words, building on existing
linguistic data. Come here for a dictionary '''
from langmaker.morphology import Morphology

class Lexeme(object):
    ''' works with words '''
    dictionary = {}

    def __init__(self, morphology=None):
        self.morphology = morphology or Morphology()

    def get_lemma(self):
        ''' get the dictionary form of a lexeme '''
        return self.morphology.generate_lemma()

    def get_lexeme_set(self):
        ''' produce the words for a lexeme (ie: ['run', 'ran']) '''
        # TODO: actually produce the set of words for a lexeme
        return [self.get_word()]

    def get_word(self):
        ''' create a word (lemma or lexeme) '''
        # TODO: do some actual morphology
        return self.get_lemma()

    def translate(self, english_word):
        ''' lookup or create a translation for an english word '''
        if not english_word in self.dictionary:
            self.dictionary[english_word] = self.get_lemma()
        return self.dictionary[english_word]

if __name__ == '__main__':
    builder = Lexeme()
    for word in ['cat', 'flower', 'hate', 'blue', 'sprint', 'quickly']:
        print('%s: %s' % (word, builder.translate(word)))
