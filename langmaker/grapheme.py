''' Translate phonemes into graphemes '''
import json
import random
from langmaker import DATA
from langmaker.phoneme import Phoneme
from langmaker.lemma import Lemma

class Grapheme(object):
    ''' produce graphemes for lemmas '''

    def __init__(self, phonemes=None, conversions=None, lemmas=None):
        if phonemes and not conversions:
            raise ValueError('Conversions must be provided with phonemes')
        self.lemmas = lemmas or Lemma()
        self.phonemes = phonemes or Phoneme()

        data = json.loads(open('%s/graphemes.json' % DATA).read())
        self.conversions = conversions or data['conversions']

    def write_lemma(self, lemma=None):
        ''' convert phonemes into graphemes '''
        lemma = lemma or self.lemmas.get_lemma()
        graphemes = []
        for phoneme in lemma.split('/'):
            try:
                options = self.conversions[phoneme]
                graphemes.append(random.choice(options))
            except KeyError:
                graphemes.append(phoneme)
        return ''.join(graphemes)

if __name__ == '__main__':
    builder = Grapheme()
    for _ in range(10):
        print(builder.write_lemma())
