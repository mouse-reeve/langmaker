''' Morphological rules for grammar and word construction '''
from numpy.random import choice
from langmaker.morpheme import Morpheme
from langmaker import pos

class Morphology(object):
    ''' interrelated grammar and word structures '''

    def __init__(self, morphemes=None):
        self.morphemes = morphemes or Morpheme()

    def decline(self, word, word_pos, tags):
        ''' declension for inflected nouns, pronounces, adjectives, and determiners '''
        # TODO: define tags
        # TODO: consider interaction between morphological tags
        if 'pl' in tags and word_pos in ['NN', 'NNP']:
            word += self.morphemes.get_affix('pl')

        if 'f' in tags and word_pos in ['JJ']:
            word += self.morphemes.get_affix('f')

        return word

    def inflect(self, lemma, word_pos, tags):
        ''' inflect a word based on grammatical variables '''
        # yeah, build n inflection engine, no problem
        # TODO: account for all kinds of inflection
        if not word_pos in pos:
            raise KeyError('invalid part of speech')
        # TODO: which type of inflection applies to which pos
        # noun, pronoun, adjective, determiner
        if word_pos in ['NN', 'NNP', 'JJ', 'PDT']:
            return self.decline(lemma, word_pos, tags)
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
        lemma_pl = builder.inflect(sample_lemma, 'NN', ['pl'])
        lemma_infl = builder.inflect(sample_lemma, 'JJ', ['f'])
        print(sample_lemma)
        print(lemma_pl)
        print(lemma_infl)
