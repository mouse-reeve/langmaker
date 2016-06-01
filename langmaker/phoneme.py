''' Generate linguistically consistent phonemes '''

class Phoneme(object):
    ''' create phonemes '''

    def __init__(self):
        self.phonemes = []

    def generate_phonemes(self):
        ''' produces a complete array of transcribed phonemes'''
        self.phonemes = {
            'vowels': [],
            'consonants': []
        }
        return self.phonemes

if __name__ == '__main__':
    builder = Phoneme()
    print(builder.get_phonemes())

