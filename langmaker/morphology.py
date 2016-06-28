''' Morphological rules for grammar and word construction '''
from numpy.random import choice
from langmaker.inflectionrule import InflectionRules
from langmaker.morpheme import Morpheme
from langmaker import pos

class Morphology(object):
    ''' interrelated grammar and word structures '''

    def __init__(self, morphemes=None, rules=None):
        self.morphemes = morphemes or Morpheme()
        rules = rules if rules else [
            (['NN', 'Pl', 'Nom'], '$', '/S/')
        ]

        self.rules = InflectionRules(signatures=rules)

    def inflect(self, lemma, word_pos, tags):
        ''' inflect a word based on grammatical variables '''
        if not word_pos in pos:
            raise KeyError('invalid part of speech')

        return self.rules.apply_rule(lemma, tags)

    def generate_lemma(self, word_pos):
        ''' combine morphemes into lemmas '''
        if not word_pos in pos:
            raise KeyError('invalid part of speech')
        # TODO: intelligently join morphemes
        # TODO: meaningful morpheme count
        length = choice([1, 2], 1, p=[0.9, 0.1])[0]
        lemma = ''.join([self.morphemes.get_morpheme() for _ in range(length)])
        return '%s' % lemma

if __name__ == '__main__':
    builder = Morphology()
    for _ in range(10):
        sample_lemma = builder.generate_lemma('NN')
        lemma_pl = builder.inflect(sample_lemma, 'NN', ['NN', 'Pl', 'Nom'])
        print(sample_lemma)
        print(lemma_pl)
