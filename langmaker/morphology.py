''' Morphological rules for grammar and word construction '''
from numpy.random import choice
from langmaker.morpheme import Morpheme
from langmaker import pos

class Morphology(object):
    ''' interrelated grammar and word structures '''

    def __init__(self, morphemes=None):
        self.morphemes = morphemes or Morpheme()

    def plural(self, word, number):
        ''' plural inflection '''
        # TODO: this is terrible
        affix = ''
        # TODO: conspider multiple plurals
        if number != 1:
            affix = self.morphemes.get_affix('pl')
        # TODO: consider nonterminal plural affixes
        return word + affix

    def inflect(self, lemma, word_pos, number=None):
        ''' inflect a word based on grammatical variables '''
        # yeah, build n inflection engine, no problem
        # TODO: account for all kinds of inflection
        if not word_pos in pos:
            raise KeyError('invalid part of speech')
        # TODO: which type of inflection applies to which pos
        if number: # TODO: and this pos pluralizes
            return self.plural(lemma, number)
        return lemma

    def generate_lemma(self):
        ''' combine morphemes into lemmas '''
        # TODO: intelligently join morphemes
        # TODO: meaningful morpheme count
        length = choice([1, 2], 1, p=[0.9, 0.1])[0]
        return '/'.join([self.morphemes.get_morpheme() for _ in range(length)])

if __name__ == '__main__':
    builder = Morphology()
    for _ in range(10):
        sample_lemma = builder.generate_lemma()
        lemma_infl = builder.inflect(sample_lemma, 'NN', number=2)
        print(sample_lemma)
        print(lemma_infl)
