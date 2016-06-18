''' test word generator '''
import unittest
from unittest import TestCase
from unittest.mock import MagicMock

from langmaker.lexeme import Lexeme
from langmaker.morphology import Morphology

morphologyMock = Morphology
morphologyMock.generate_lemma = MagicMock(return_value='mor')
morphologyMock.inflect = MagicMock(return_value='mor')
instance = Lexeme(morphology=morphologyMock)


class LexemeTest(TestCase):
    ''' word tests '''

    def test_get_word(self):
        ''' tests that a word in build from morphemes '''
        word = instance.get_word()
        self.assertTrue(len(word) > 0 and 'mor' in word)

    def test_translate(self):
        ''' tests that translation occurs and is persistant '''
        translation = instance.translate('cat', 'NN')
        self.assertTrue(len(translation) > 0 and 'mor' in translation)

        lookup = instance.translate('cat', 'NN')
        self.assertEqual(translation, lookup)


if __name__ == '__main__':
    unittest.main()
