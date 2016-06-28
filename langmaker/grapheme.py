''' Translate phonemes into graphemes '''
from langmaker import cmu_graphemes
from langmaker.phoneme import Phoneme
from langmaker.transcriptionrule import TranscriptionRules

class Grapheme(object):
    ''' produce graphemes for words '''
    rules = TranscriptionRules()

    def __init__(self, phonemes=None, conversions=None, rules=None):
        if phonemes and not conversions:
            raise ValueError('Conversions must be provided with phonemes')
        conversions = conversions or cmu_graphemes['conversions']

        self.phonemes = phonemes or Phoneme()

        # patterns in phoneme -> grapheme conversion
        if rules:
            for rule in rules:
                self.rules.add_rule(rule[0], rule[1])

        # conversions are one-to-one phoneme to grapheme conversions
        # they're less "correct" but necessary to avoid untranscribed edge cases
        for conversion in conversions:
            self.rules.add_rule(conversion[0], conversion[1])


    def write_word(self, word):
        ''' convert phonemes into graphemes '''
        written = self.rules.apply_rules(word)
        return ''.join(written.split('/'))

if __name__ == '__main__':
    builder = Grapheme()
    print(builder.write_word('T/AH/M/EY/T/OW'))
