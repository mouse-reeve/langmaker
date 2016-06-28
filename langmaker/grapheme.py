''' Translate phonemes into graphemes '''
from langmaker.phoneme import Phoneme
from langmaker.transcriptionrule import TranscriptionRules

class Grapheme(object):
    ''' produce graphemes for words '''
    rules = TranscriptionRules()

    def __init__(self, phonemes=None, rules=None):
        self.phonemes = phonemes or Phoneme()

        # patterns in phoneme -> grapheme conversion
        if not rules:
            rules = self.generate_rules()
        for rule in rules:
            self.rules.add_rule(rule[0], rule[1])

        # one-to-one phoneme->grapheme, to avoid missing phonemes
        for conversion in self.phonemes.get_phonemes():
            self.rules.add_rule(conversion[0], conversion[1])


    def write_word(self, word):
        ''' convert phonemes into graphemes '''
        written = self.rules.apply_rules(word)
        return ''.join(written.split('/'))


    def generate_rules(self):
        ''' generate some transcriptions rules '''
        # TODO
        return [
            (r'/L/IY/$', '/ly/')
        ]

if __name__ == '__main__':
    builder = Grapheme()
    print(builder.write_word('T/AH/M/EY/T/OW'))
