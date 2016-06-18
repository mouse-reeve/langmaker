''' System for generating lexemes, lemmas, and words, building on existing
linguistic data. Come here for a dictionary '''
from langmaker.morphology import Morphology

class Lexeme(object):
    ''' works with words '''
    dictionary = {}

    def __init__(self, morphology=None):
        self.morphology = morphology or Morphology()

    def get_lemma(self, pos):
        ''' get the dictionary form of a lexeme '''
        # TODO: consider part of speech
        return self.morphology.generate_lemma(pos)

    def get_lexeme_set(self):
        ''' produce the words for a lexeme (ie: ['run', 'ran']) '''
        # TODO: actually produce the set of words for a lexeme
        return [self.get_word()]

    def get_word(self, pos='NN', tags=None):
        ''' create a word (lemma or lexeme) '''
        lemma = self.get_lemma(pos)

        tags = [] if not tags else tags
        return self.morphology.inflect(lemma, pos, tags)

    def translate(self, english_word, pos):
        ''' lookup or create a translation for an english word '''
        if not english_word in self.dictionary:
            self.dictionary[english_word] = self.get_lemma(pos)
        return self.dictionary[english_word]

if __name__ == '__main__':
    builder = Lexeme()
    translate = [
        ('cat', 'NN'),
        ('flower', 'NN'),
        ('hate', 'VB'),
        ('blue', 'JJ'),
        ('sprint', 'VB'),
        ('quickly', 'RB')
    ]
    for word in translate:
        print('%s: %s' % (word[0], builder.translate(word[0], word[1])))
