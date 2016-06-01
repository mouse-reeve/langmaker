''' test word generator '''
import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from langmaker.word import Word, Morpheme

wordMock = Morpheme
wordMock.get_morpheme = MagicMock(return_value='mor')
instance = Word(wordMock)


class WordTest(TestCase):
    ''' word tests '''

    def test_get_word(self):
        ''' tests that a word in build from morphemes '''
        word = instance.get_word()
        self.assertTrue(len(word) > 0 and 'mor' in word)


if __name__ == '__main__':
    unittest.main()
