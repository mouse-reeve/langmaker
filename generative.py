''' a completely generated language '''
from langmaker.phoneme import Phoneme
from langmaker.syllable import Syllable
from langmaker.morpheme import Morpheme
from langmaker.morphology import Morphology
from langmaker.lexeme import Lexeme
from langmaker.grapheme import Grapheme

phoneme = Phoneme()
syllable = Syllable(phonemes=phoneme)
morpheme = Morpheme(syllables=syllable)
morphology = Morphology(morphemes=morpheme)
lexeme = Lexeme(morphology=morphology)
grapheme = Grapheme(phonemes=phoneme)

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
