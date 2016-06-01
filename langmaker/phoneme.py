''' Generate linguistically consistent phonemes '''
import random

# XXX: this class produces test data at this time
class Phoneme(object):
    ''' create phonemes '''

    def __init__(self, consonants=None, vowels=None):
        # should be comprehensive, or pulled from a transcription class
        self.consonants = None
        self.vowels = None

        self.phoneme_set = {
            'vowels': ['a', 'e', 'i', 'o', 'u', 'y'],
            'consonants': ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r',
                           's', 't', 'v', 'w', 'x', 'z']
        }
        self.consonants = consonants or self.generate_consonants()
        self.vowels = vowels or self.generate_vowels()

    def generate_consonants(self):
        ''' generates a selection of consonant phonemes '''
        # TODO: select a meaningful phoneme set
        return self.consonants or self.phoneme_set['consonants']

    def generate_vowels(self):
        ''' generates a selection of vowel phonemes '''
        # TODO: select a meaningful phoneme set
        return self.vowels or self.phoneme_set['vowels']

    def get_phonemes(self):
        ''' return a complete list of phonemes '''
        return (self.consonants, self.vowels)

    def get_vowel(self):
        ''' retrieve a random vowel phoneme '''
        return random.choice(self.vowels)

    def get_consonant(self):
        ''' retrieve a random consonant phoneme '''
        return random.choice(self.consonants)


if __name__ == '__main__':
    builder = Phoneme()
    print(builder.get_phonemes())

