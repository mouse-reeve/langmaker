''' Generate linguistically consistent phonemes '''
import random
from numpy.random import choice

from langmaker import cmu_phonemes

class Phoneme(object):
    ''' create phonemes '''

    def __init__(self, consonants=None, consonant_clusters=None,
                 vowels=None, frequency=None):

        # TODO: this is a bad approach
        data = {}
        if not consonants or not vowels:
            data = cmu_phonemes
        self.consonants = consonants or data['consonants']
        self.vowels = vowels or data['vowels']
        self.consonant_clusters = consonant_clusters or \
                                  data['consonant_clusters']

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

    def get_vowel(self):
        ''' retrieve a random vowel phoneme '''
        if self.frequency:
            return choice(self.vowels, 1, p=self.vowel_frequency)[0]
        else:
            return random.choice(self.vowels)

    def get_consonant(self):
        ''' retrieve a random consonant phoneme '''
        if self.frequency:
            return choice(self.consonants, 1, p=self.consonant_frequency)[0]
        else:
            return random.choice(self.consonants)

    def get_consonant_cluster(self):
        ''' retrieve a list of cluster-able consonants '''
        return random.choice(self.consonant_clusters)

    def get_by_key(self, key):
        ''' get a letter by type using cfg keys '''
        keys = {
            'c': self.get_consonant,
            'cc': self.get_consonant_cluster,
            'v': self.get_vowel
        }
        try:
            return keys[key]()
        except KeyError:
            return ''


if __name__ == '__main__':
    builder = Phoneme()
    print(builder.get_vowel())
    print(builder.get_consonant())

