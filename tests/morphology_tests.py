''' test morphology generator '''
import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from langmaker.morphology import Morphology, Morpheme

morphemeMock = Morpheme
morphemeMock.get_morpheme = MagicMock(return_value='mor')
instance = Morphology(morphemes=morphemeMock)

class MorphologyTest(TestCase):
    ''' morphology tests '''

    def test_generate_word(self):
        ''' tests that a word in build from morphemes '''
        word = instance.generate_word()
        self.assertTrue(len(word) > 0 and 'mor' in word)


if __name__ == '__main__':
    unittest.main()

