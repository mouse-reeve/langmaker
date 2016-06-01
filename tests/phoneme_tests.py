''' test phoneme generator '''
import unittest
from unittest import TestCase

from langmaker.phoneme import Phoneme

specified = Phoneme(consonants=['p'], vowels=['o'])
unspecified = Phoneme()


class PhonemeTest(TestCase):
    ''' phoneme tests '''

    def test_generate_specified(self):
        ''' tests fetching consonants '''
        consonants = specified.generate_consonants()
        self.assertEqual(consonants, ['p'])

        vowels = specified.generate_vowels()
        self.assertEqual(vowels, ['o'])

    def test_generate_unspecified(self):
        ''' test automatic phoneme production '''
        consonants = unspecified.generate_consonants()
        self.assertTrue(consonants <= unspecified.phoneme_set['consonants'])

        vowels = unspecified.generate_vowels()
        self.assertTrue(vowels <= unspecified.phoneme_set['vowels'])

    def test_get_consonant(self):
        ''' retrieve a consonant '''
        consonant = specified.get_consonant()
        self.assertEqual(consonant, 'p')

    def test_get_vowel(self):
        ''' retrieve a vowel '''
        vowel = specified.get_vowel()
        self.assertEqual(vowel, 'o')

    def test_get_phonemes(self):
        ''' retrieve the entire set '''
        phonemes = specified.get_phonemes()
        self.assertEqual(phonemes, (['p'], ['o']))


if __name__ == '__main__':
    unittest.main()
