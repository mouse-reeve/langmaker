''' Generate linguistically consistent syllables '''
import random
import re
from nltk import CFG
from nltk.parse.generate import generate

from langmaker.phoneme import Phoneme

class Syllable(object):
    ''' combine phonemes into syllables '''

    def __init__(self, phonemes=None, onset=None, coda=None):
        self.phonemes = phonemes or Phoneme()

        # use CFG to structure syllables
        if onset == None: # optional onset
            onset = 'C | CC | \' \''
        elif onset: # mandatory onset
            onset = 'C | CC'
        else: # no onset
            onset = '\' \''

        if coda == None: # optional coda
            coda = 'C | \' \''
        elif coda: # mandatory coda
            coda = 'C'
        else: # no coda
            coda = '\' \''

        # nucleus is always present

        delimiter = '\' | \''
        grammar = '''
        S -> O V K
        O -> %s
        K -> %s
        C -> \'%s\'
        CC -> \'%s\'
        V -> \'%s\'
        ''' % (onset, coda,
               delimiter.join(self.phonemes.consonants),
               delimiter.join(self.phonemes.consonant_clusters),
               delimiter.join(self.phonemes.vowels))
        self.grammar = CFG.fromstring(grammar)
        self.syllables = self.generate_syllables()

    def generate_syllables(self):
        ''' every possible syllable for the given phonemes and grammar '''
        # spaces, which are only there for NLTK's sake, are removed
        return [re.sub(' ', '', ''.join(s)) for s in generate(self.grammar, depth=4)]

    def get_syllable(self):
        ''' create a syllable '''
        return random.choice(self.syllables)

if __name__ == '__main__':
    builder = Syllable()
    print(builder.get_syllable())
