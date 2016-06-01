''' test morpheme generator '''
import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from langmaker.morpheme import Morpheme, Syllable

syllableMock = Syllable
syllableMock.get_syllable = MagicMock(return_value='sy')
instance = Morpheme(syllableMock)


class MorphemeTest(TestCase):
    ''' morpheme tests '''

    def test_set_length_morpheme(self):
        ''' tests specifying the length of a morpheme '''
        morpheme = instance.get_morpheme(length=1)
        self.assertEqual(morpheme, 'sy')

        morpheme = instance.get_morpheme(length=5)
        self.assertEqual(morpheme, 'sysysysysy')

    def test_invalid_length_morpheme(self):
        ''' edge cases for bad len input '''
        morpheme = instance.get_morpheme(length=0)
        self.assertTrue(len(morpheme) > 0 and 'sy' in morpheme)

    def test_random_morpheme(self):
        ''' let the class decide the length of the morpheme '''
        morpheme = instance.get_morpheme()
        self.assertTrue(len(morpheme) > 0 and 'sy' in morpheme)


if __name__ == '__main__':
    unittest.main()
