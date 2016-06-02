''' Generate linguistically consistent phonemes '''
import random

# XXX: this class produces test data at this time
class Phoneme(object):
    ''' create phonemes '''

    def __init__(self, consonants=None, vowels=None):
        # should be comprehensive, or pulled from a transcription class
        self.consonants = None
        self.vowels = None

        # TODO: this is a bad approach
        self.consonants = consonants or ['b', 'c', 'ch', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
                           'r', 's', 't', 'th', 'v', 'w', 'x', 'z']
        self.vowels = vowels or ['a', 'e', 'i', 'o', 'u', 'y']
        self.consonant_clusters = ['str', 'cr', 'tr', 'pr', 'spr']

    def get_vowel(self):
        ''' retrieve a random vowel phoneme '''
        return random.choice(self.vowels)

    def get_consonant(self):
        ''' retrieve a random consonant phoneme '''
        return random.choice(self.consonants)

    def get_cluster(self):
        ''' retrieve a list of cluster-able consonants '''
        return random.choice(self.consonant_clusters)


if __name__ == '__main__':
    builder = Phoneme()
    print(builder.get_phonemes())

