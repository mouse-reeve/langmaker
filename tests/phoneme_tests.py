''' test phoneme generator '''
import unittest
from unittest import TestCase

from langmaker.phoneme import Phoneme

instance = Phoneme(consonants=['p'], vowels=['o'])


class PhonemeTest(TestCase):
    ''' phoneme tests '''

    def test_get_consonant(self):
        ''' retrieve a consonant '''
        consonant = instance.get_consonant()
        self.assertEqual(consonant, 'p')

    def test_get_vowel(self):
        ''' retrieve a vowel '''
        vowel = instance.get_vowel()
        self.assertEqual(vowel, 'o')

    def test_get_consonant_clusters(self):
        ''' retrieve consonant clusters '''
        # nothing here to test right now
        pass


if __name__ == '__main__':
    unittest.main()
