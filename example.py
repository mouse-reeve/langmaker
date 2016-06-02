''' a sample file of a fully customized language generation process '''
from langmaker.phoneme import Phoneme
from langmaker.syllable import Syllable
from langmaker.morpheme import Morpheme
from langmaker.lemma import Lemma
from langmaker.grapheme import Grapheme

consonants = ['b', 'p', 'l']
vowels = ['o', 'oo']

phoneme = Phoneme(consonants=consonants, vowels=vowels, consonant_clusters=['b/l', 'p/l'])
syllable = Syllable(phonemes=phoneme, coda=True)
morpheme = Morpheme(syllables=syllable)
lemma = Lemma(morphemes=morpheme)
conversions = {p: p for p in consonants + vowels}
grapheme = Grapheme(phonemes=phoneme, lemmas=lemma, conversions=conversions)

for _ in range(10):
    print(grapheme.write_lemma())
