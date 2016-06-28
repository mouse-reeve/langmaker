''' a sample file of a fully customized language generation process '''
from langmaker import cmu_phonemes, cmu_graphemes

from langmaker.phoneme import Phoneme
from langmaker.syllable import Syllable
from langmaker.morpheme import Morpheme
from langmaker.morphology import Morphology
from langmaker.lexeme import Lexeme
from langmaker.grapheme import Grapheme

consonants = cmu_phonemes['consonants']
clusters = cmu_phonemes['consonant_clusters']
vowels = cmu_phonemes['vowels']

inflection_rules = [
    # PoS default endings
    (['RB'], r'$', '/L/IY'),

    # Pluralization rules
    (['NN', 'Pl'], r'$', '/S'),

    # Declension
    (['PRP', 'Sg', 'Masc', 'Acc'], r'^(.*)\/.*', r'/\1/IH/M'),
    (['PRP', 'Sg', 'Fem', 'Acc'], r'^.*\/(.*)', r'\1/R')
]

transcription_rules = [
    (r'L/IY$', 'ly')
]

phoneme = Phoneme(consonants=consonants, vowels=vowels,
                  consonant_clusters=clusters)

# english has highly flexible phonemes - coda and onset are both optional
syllable = Syllable(phonemes=phoneme)
morpheme = Morpheme(syllables=syllable)
morphology = Morphology(morphemes=morpheme, rules=inflection_rules)
lexeme = Lexeme(morphology=morphology)

grapheme = Grapheme(phonemes=phoneme, rules=transcription_rules,
                    conversions=cmu_graphemes['conversions'])

translate = [
    ('noun', 'NN'),
    ('noun', 'NN'),
    ('verb', 'VB'),
    ('adjective', 'JJ'),
    ('verb', 'VB'),
    ('adverb', 'RB'),
    ('m. pron', 'PRP'),
    ('f. pron', 'PRP')
]
for word in translate:
    translated = lexeme.translate(word[0], word[1])
    if word[1] == 'RB':
        translated = morphology.inflect(translated, word[1], [word[1]])
        print('%s: %s' % (word[0], grapheme.write_word(translated)))
    else:
        print('%s: %s' % (word[0], grapheme.write_word(translated)))

    if word[1] == 'NN':
        inflected = morphology.inflect(translated, word[1], ['NN', 'Pl'])
        print('      pl: %s' % grapheme.write_word(inflected))

    if word[0] == 'm. pron':
        inflected = morphology.inflect(translated, word[1],
                                       ['PRP', 'Sg', 'Masc', 'Acc'])
        print('      akk: %s' % grapheme.write_word(inflected))

    if word[0] == 'f. pron':
        inflected = morphology.inflect(translated,
                                       word[1], ['PRP', 'Sg', 'Fem', 'Acc'])
        print('      akk: %s' % grapheme.write_word(inflected))

