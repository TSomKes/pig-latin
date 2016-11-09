#!/usr/bin/env python3


import unittest

from translator import Translator


class TestTranslator(unittest.TestCase):

    def test_IsVowel_vowels(self):
        self.assertTrue(Translator.IsVowel('a'))
        self.assertTrue(Translator.IsVowel('A'))

    def test_IsVowel_consonants(self):
        self.assertFalse(Translator.IsVowel('b'))
        self.assertFalse(Translator.IsVowel('B'))

    def test_IsVowel_empty(self):
        self.assertFalse(Translator.IsVowel(''))

    def test_IsVowel_nonalpha(self):
        self.assertFalse(Translator.IsVowel(' '))
        self.assertFalse(Translator.IsVowel('-'))
        self.assertFalse(Translator.IsVowel('1'))

    def test_Translate_singleword_initialvowel(self):
        t = Translator()
        self.assertEqual(t.Translate("aardvark"), "aardvarkway")

    def test_Translate_singleword_initialconsonant(self):
        t = Translator()
        self.assertEqual(t.Translate("foo"), "oofay")

    def test_Translate_multiplewords(self):
        t = Translator()
        self.assertEqual(t.Translate("this is a test"),
                                     "isthay isway away esttay")

if __name__ == "main":
    unittest.main()
