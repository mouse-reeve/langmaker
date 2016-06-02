''' Translate phonemes into graphemes '''
from langmaker.phoneme import Phoneme

class Grapheme(object):
    ''' produce graphemes for words '''

    def __init__(self, phonemes=None, conversions=None):
        if phonemes and not conversions:
            raise ValueError('Conversions must be provided with phonemes')
        self.phonemes = phonemes or Phoneme()
        self.conversions = conversions or []
