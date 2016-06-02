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

        # based on the "typical model"
        grammar = '''
        S -> O V K
        O -> %s
        K -> %s
        C -> \'c\'
        CC -> \'cc\'
        V -> \'v\'
        ''' % (onset, coda)
        self.grammar = CFG.fromstring(grammar)
        self.syllables = self.generate_syllables()

    def generate_syllables(self):
        ''' every possible syllable for the given phonemes and grammar '''
        # spaces, which are only there for NLTK's sake, are removed
        return [re.sub(' ', '', '/'.join(s)) for s in generate(self.grammar, depth=4)]

    def get_syllable(self):
        ''' create a syllable '''
        structure = random.choice(self.syllables).split('/')
        syllable = [self.phonemes.get_by_key(s) for s in structure if s]
        return '/'.join(syllable)


if __name__ == '__main__':
    builder = Syllable()
    for _ in range(10):
        print(builder.get_syllable())
