''' Generate linguistically consistent phonemes '''
import random
from numpy.random import choice

from langmaker import ipa_phonemes
from langmaker import cmu_phonemes

class Phoneme(object):
    ''' create phonemes '''
    consonants = []
    vowles = []

    def __init__(self, phonemes=None, frequency=None):
        if phonemes:
            self.select_phonemes(phonemes)
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


    def select_phonemes(self, phonemes):
        ''' use a given list of ipa phonemes  '''
        consonants = {i[0]: i for i in ipa_phonemes['consonants']['pulmonic']}
        for phoneme in phonemes['consonants']:
            self.consonants.append(consonants[phoneme])


    def generate(self):
        ''' select a phonemeset '''
        # 73% of language have only pulmonic consonants
        self.consonants = ipa_phonemes['consonants']['pulmonic']
        self.vowels = cmu_phonemes['vowels']


if __name__ == '__main__':
    builder = Phoneme()
    print(builder.get_vowel())
    print(builder.get_consonant())
