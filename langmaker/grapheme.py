''' Translate phonemes into graphemes '''
import json
import random
from langmaker import DATA
from langmaker.phoneme import Phoneme
from langmaker.lexeme import Lexeme

class Grapheme(object):
    ''' produce graphemes for words '''

    def __init__(self, phonemes=None, conversions=None, lexemes=None):
        if phonemes and not conversions:
            raise ValueError('Conversions must be provided with phonemes')
        self.lexemes = lexemes or Lexeme()
        self.phonemes = phonemes or Phoneme()

        data = json.loads(open('%s/graphemes.json' % DATA).read())
        self.conversions = conversions or data['conversions']

    def write_word(self, word=None):
        ''' convert phonemes into graphemes '''
        word = word or self.lexemes.get_word()
        graphemes = []
        for phoneme in word.split('/'):
            try:
                options = self.conversions[phoneme]
                graphemes.append(random.choice(options))
            except KeyError:
                graphemes.append(phoneme)
        return ''.join(graphemes)

if __name__ == '__main__':
    builder = Grapheme()
    for _ in range(10):
        print(builder.write_word())
