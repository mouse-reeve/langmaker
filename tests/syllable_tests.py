''' test syllable generator '''
import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from langmaker.syllable import Syllable, Phoneme

phonemeMock = Phoneme
phonemeMock.get_by_key = MagicMock(return_value='o')


class SyllableTest(TestCase):
    ''' syllable tests '''

    def test_default_grammar(self):
        ''' NLTK generated syllables '''
        instance = Syllable(phonemes=phonemeMock)
        syllables = instance.syllables
        self.assertEqual(syllables, ['c|v|c', 'c|v|', 'cc|v|c', 'cc|v|', '|v|c', '|v|'])

    def test_onset_states(self):
        ''' NLTK generated syllables with onset flag'''
        instance = Syllable(phonemes=phonemeMock, onset=True)
        syllables = instance.syllables
        self.assertEqual(syllables, ['c|v|c', 'c|v|', 'cc|v|c', 'cc|v|'])

        instance = Syllable(phonemes=phonemeMock, onset=False)
        syllables = instance.syllables
        self.assertEqual(syllables, ['|v|c', '|v|'])

    def test_coda_states(self):
        ''' NLTK generated syllables with coda flag'''
        instance = Syllable(phonemes=phonemeMock, coda=True)
        syllables = instance.syllables
        self.assertEqual(syllables, ['c|v|c', 'cc|v|c', '|v|c'])

        instance = Syllable(phonemes=phonemeMock, coda=False)
        syllables = instance.syllables
        self.assertEqual(syllables, ['c|v|', 'cc|v|', '|v|'])


if __name__ == '__main__':
    unittest.main()
