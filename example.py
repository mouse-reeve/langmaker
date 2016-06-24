''' a sample file of a fully customized language generation process '''
from langmaker.phoneme import Phoneme
from langmaker.syllable import Syllable
from langmaker.morpheme import Morpheme
from langmaker.morphology import Morphology
from langmaker.lexeme import Lexeme
from langmaker.grapheme import Grapheme

consonants = ['b', 'p', 'l', 'f']
vowels = ['o', 'oo', 'ou', 'oio']
inflection_rules = [
    (['NN', 'Pl'], r'$', 'ses')
]

phoneme = Phoneme(consonants=consonants, vowels=vowels,
                  consonant_clusters=['b/l', 'p/l', 'f/l'])
syllable = Syllable(phonemes=phoneme, coda=True)
morpheme = Morpheme(syllables=syllable)
morphology = Morphology(morphemes=morpheme, rules=inflection_rules)
lexeme = Lexeme(morphology=morphology)

conversions = {p: [p] for p in consonants + vowels}
grapheme = Grapheme(phonemes=phoneme, lexemes=lexeme, conversions=conversions)

translate = [
    ('cat', 'NN'),
    ('flower', 'NN'),
    ('hate', 'VB'),
    ('blue', 'JJ'),
    ('sprint', 'VB'),
    ('quickly', 'RB')
]
for word in translate:
    translated = lexeme.translate(word[0], word[1])
    print('%s: %s' % (word[0], grapheme.write_word(translated)))

    if word[1] == 'NN':
        inflected = morphology.inflect(translated, word[1], ['NN', 'Pl'])
        print('      pl: %s' % grapheme.write_word(inflected))
