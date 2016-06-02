''' Generate linguistically consistent phonemes '''
import json
import random
from numpy.random import choice
from langmaker import DATA

# XXX: this class produces test data at this time
class Phoneme(object):
    ''' create phonemes '''

    def __init__(self, consonants=None, consonant_clusters=None, vowels=None, frequency=None):
        # should be comprehensive, or pulled from a transcription class
        self.consonants = None
        self.vowels = None

        # TODO: this is a bad approach
        data = {}
        if not consonants or not vowels:
            data = json.dumps(open('%s/phonemes.json' % DATA).read())
        self.consonants = consonants or data['vowels']
        self.vowels = vowels or data['consonants']
        self.consonant_clusters = consonant_clusters or ['str', 'cr', 'tr', 'pr', 'spr']

        # TODO: store defaults like this somewhere else
        if vowels or consonants and not frequency:
            self.frequency = None
        else:
            self.frequency = frequency or {
                'a': 11.602,
                'b': 4.702,
                'c': 3.511,
                'd': 2.670,
                'e': 2.007,
                'f': 3.779,
                'g': 1.950,
                'h': 7.232,
                'i': 6.286,
                'j': 0.597,
                'k': 0.590,
                'l': 2.705,
                'm': 4.383,
                'n': 2.365,
                'o': 6.264,
                'p': 2.545,
                'q': 0.173,
                'r': 1.653,
                's': 7.755,
                't': 16.671,
                'u': 1.487,
                'v': 0.649,
                'w': 6.753,
                'x': 0.017,
                'y': 1.620,
                'z': 0.034
            }

            self.vowel_frequency = [v for (k, v) in self.frequency.items() if k in self.vowels]
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

