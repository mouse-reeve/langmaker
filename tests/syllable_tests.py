''' test syllable generator '''
import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from langmaker.syllable import Syllable, Phoneme

syllableMock = Phoneme
syllableMock.get_consonant = MagicMock(return_value='p')
syllableMock.get_vowel = MagicMock(return_value='o')
instance = Syllable(syllableMock)


class SyllableTest(TestCase):
    ''' syllable tests '''

    def test_given_structure(self):
        ''' tests specifying the length of a syllable '''
        # TODO: the code isn't in a state for this yet
        pass


if __name__ == '__main__':
    unittest.main()
