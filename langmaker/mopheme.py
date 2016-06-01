''' Generate linguistically consistent morphemes '''

class Morpheme(object):
    ''' combine syllables into morphemes '''

    def __init__(self):
        self.syllables = []

    def generate_morpheme(self):
        ''' create a morpheme '''
        return 'hi' + ''.join(self.syllables)

if __name__ == '__main__':
    builder = Morpheme()
    print(builder.generate_morpheme())
