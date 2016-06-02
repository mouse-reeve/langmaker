''' test syllable generator '''
import unittest
from unittest import TestCase

from langmaker.syllable import Syllable, Phoneme

phonemeMock = Phoneme
phonemeMock.consonants = ['p']
phonemeMock.consonant_clusters = ['pr']
phonemeMock.vowels = ['o']


class SyllableTest(TestCase):
    ''' syllable tests '''

    def test_default_grammar(self):
        ''' NLTK generated syllables '''
        instance = Syllable(phonemes=phonemeMock)
        syllables = instance.syllables
        self.assertEqual(syllables, ['pop', 'po', 'prop', 'pro', 'op', 'o'])

    def test_onset_states(self):
        ''' NLTK generated syllables with onset flag'''
        instance = Syllable(phonemes=phonemeMock, onset=True)
        syllables = instance.syllables
        self.assertEqual(syllables, ['pop', 'po', 'prop', 'pro'])

        instance = Syllable(phonemes=phonemeMock, onset=False)
        syllables = instance.syllables
        self.assertEqual(syllables, ['op', 'o'])

    def test_coda_states(self):
        ''' NLTK generated syllables with coda flag'''
        instance = Syllable(phonemes=phonemeMock, coda=True)
        syllables = instance.syllables
        self.assertEqual(syllables, ['pop', 'prop', 'op'])

        instance = Syllable(phonemes=phonemeMock, coda=False)
        syllables = instance.syllables
        self.assertEqual(syllables, ['po', 'pro', 'o'])

    def test_get_syllable(self):
        ''' pick a syllablle '''
        instance = Syllable(phonemes=phonemeMock)
        syllable = instance.get_syllable()
        self.assertTrue(syllable in ['pop', 'po', 'prop', 'pro', 'op', 'o'])


if __name__ == '__main__':
    unittest.main()
