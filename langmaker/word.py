''' System for generating words, buildin on existing linguistic data '''

class Word(object):
    ''' the dumbest to generate a word - just random letters '''

    def __init__(self):
        self.morphemes = []

    def generate_word(self):
        ''' create a word '''
        return 'hi' + ''.join(self.morphemes)

if __name__ == '__main__':
    wordbuilder = Word()
    print(wordbuilder.generate_word())
