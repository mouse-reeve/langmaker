''' a sample file of a fully customized language generation process '''
from langmaker import cmu_phonemes

from langmaker.phoneme import Phoneme
from langmaker.syllable import Syllable
from langmaker.morpheme import Morpheme
from langmaker.morphology import Morphology
from langmaker.lexeme import Lexeme
from langmaker.grapheme import Grapheme

inflection_rules = [
    # PoS default endings
    (['RB'], r'$', '/L//IY/'),

    # Pluralization rules
    (['NN', 'Pl'], r'$', '/S/'),

    # Declension
    (['PRP', 'Sg', 'Masc', 'Acc'], r'^(.*)\/[A-Z]*\/$', r'\1/IH//M/'),
    (['PRP', 'Sg', 'Fem', 'Acc'], r'^.*\/(.*)', r'\1/R/'),

    # Conjugation
    # -- 3rd person signular present tense
    (['VB', 'Sg3', 'Prs'], r'$', '/S/'),
    # - past tense
    (['VB', 'Pst'], r'$', '/EH//D/')
]

transcription_rules = [
    (r'/L/IY/$', '/ly/')
]

phoneme = Phoneme(phonemes=cmu_phonemes)

# english has highly flexible phonemes - coda and onset are both optional
syllable = Syllable(phonemes=phoneme)
morpheme = Morpheme(syllables=syllable)
morphology = Morphology(morphemes=morpheme, rules=inflection_rules)
lexeme = Lexeme(morphology=morphology)

grapheme = Grapheme(phonemes=phoneme, rules=transcription_rules)

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
        print('      acc: %s' % grapheme.write_word(inflected))

    if word[0] == 'f. pron':
        inflected = morphology.inflect(translated,
                                       word[1], ['PRP', 'Sg', 'Fem', 'Acc'])
        print('      acc: %s' % grapheme.write_word(inflected))

print('she promptly killed him')
sentence = [
    ['he', 'PRP', []],
    ['prompt', 'RB', []],
    ['kill', 'VB', ['Pst']],
    ['he', 'PRP', ['Sg', 'Masc', 'Acc']]
]
after = []
for word in sentence:
    print('-----')
    print(word)
    translated = lexeme.translate(word[0], word[1])
    print(translated)
    translated = morphology.inflect(translated, word[1], [word[1]] + word[2])
    print(translated)
    translated = grapheme.write_word(translated)
    print(translated)
    after.append(translated)

print(' '.join(after))
