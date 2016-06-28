''' Generate linguistically consistent phonemes '''
import random
from numpy.random import choice

from langmaker import cmu_phonemes

class Phoneme(object):
    ''' create phonemes '''

    def __init__(self, phonemes=None, frequency=None):
        if phonemes:
            # TODO: validate that the input phonemes have the necessary basics
            self.consonants = phonemes['consonants']
            self.vowels = phonemes['vowels']
        else:
            self.generate()

        if not frequency:
            self.frequency = None
        else:
            self.frequency = frequency
            self.vowel_frequency = [v for (k, v) in self.frequency.items()
                                    if k in self.vowels]
            self.vowel_frequency = [float(i)/sum(self.vowel_frequency) \
                                    for i in self.vowel_frequency]
            self.consonant_frequency = [v for (k, v) in self.frequency.items() \
                                        if k in self.consonants]
            self.consonant_frequency = [float(i)/sum(self.consonant_frequency) \
                                        for i in self.consonant_frequency]


    def get_phonemes(self):
        ''' a simple list of all phonemes '''
        return self.vowels + self.consonants

    def get_vowel(self):
        ''' retrieve a random vowel phoneme '''
        if self.frequency:
            return choice(self.vowels, 1, p=self.vowel_frequency)[0]
        else:
            return random.choice(self.vowels)[0]

    def get_consonant(self):
        ''' retrieve a random consonant phoneme '''
        if self.frequency:
            return choice(self.consonants, 1, p=self.consonant_frequency)[0]
        else:
            return random.choice(self.consonants)[0]

    def get_by_key(self, key):
        ''' get a letter by type using cfg keys '''
        keys = {
            'c': self.get_consonant,
            'v': self.get_vowel
        }
        try:
            return keys[key]()
        except KeyError:
            return ''

    def generate(self):
        ''' select a phonemeset '''
        self.consonants = cmu_phonemes['consonants']
        self.vowels = cmu_phonemes['vowels']

if __name__ == '__main__':
    builder = Phoneme()
    print(builder.get_vowel())
    print(builder.get_consonant())

