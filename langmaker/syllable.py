''' Generate linguistically consistent syllables '''
from langmaker.phoneme import Phoneme

class Syllable(object):
    ''' combine phonemes into syllables '''

    def __init__(self, phonemes=None):
        self.phonemes = phonemes or Phoneme()

    def get_syllable(self):
        ''' create a syllable '''
        # TODO: syllable structure assumes cv
        # should probs use CFG
        return self.phonemes.get_consonant() + self.phonemes.get_vowel()

if __name__ == '__main__':
    builder = Syllable()
    print(builder.get_syllable())
