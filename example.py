''' a sample file of a fully customized language generation process '''
from langmaker.phoneme import Phoneme
from langmaker.syllable import Syllable
from langmaker.morpheme import Morpheme
from langmaker.word import Word

phoneme = Phoneme(consonants=['b', 'p'], vowels=['o', 'oo'], consonant_clusters=['bl', 'pl', 'pr'])
syllable = Syllable(phonemes=phoneme, coda=True)
morpheme = Morpheme(syllables=syllable)
word = Word(morphemes=morpheme)

for _ in range(10):
    print(word.get_word())
