''' Generate linguistically consistent syllables '''

class Syllable(object):
    ''' combine phonemes into syllables '''

    def __init__(self):
        self.syllables = []

    def generate_syllable(self):
        ''' create a syllable '''
        return 'hi' + ''.join(self.syllables)

if __name__ == '__main__':
    builder = Syllable()
    print(builder.generate_syllable())
