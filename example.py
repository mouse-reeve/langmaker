''' a sample file of a fully customized language generation process '''
from langmaker.phoneme import Phoneme
from langmaker.syllable import Syllable
from langmaker.morpheme import Morpheme
from langmaker.morphology import Morphology
from langmaker.lexeme import Lexeme
from langmaker.grapheme import Grapheme

consonants = ['b', 'p', 'l']
vowels = ['o', 'oo']

phoneme = Phoneme(consonants=consonants, vowels=vowels, consonant_clusters=['b/l', 'p/l'])
syllable = Syllable(phonemes=phoneme, coda=True)
morpheme = Morpheme(syllables=syllable)
morphology = Morphology(morphemes=morpheme)
lexeme = Lexeme(morphology=morphology)
conversions = {p: p for p in consonants + vowels}
grapheme = Grapheme(phonemes=phoneme, lexemes=lexeme, conversions=conversions)

for _ in range(10):
    print(grapheme.write_word())
