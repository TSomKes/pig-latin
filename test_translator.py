#!/usr/bin/env python3


import unittest

import translator


class TestTranslator(unittest.TestCase):

    def test_IsVowel_vowels(self):
        self.assertTrue(translator.IsVowel('a'))
        self.assertTrue(translator.IsVowel('A'))

    def test_IsVowel_consonants(self):
        self.assertFalse(translator.IsVowel('b'))
        self.assertFalse(translator.IsVowel('B'))

    def test_IsVowel_empty(self):
        self.assertFalse(translator.IsVowel(''))

    def test_IsVowel_nonalpha(self):
        self.assertFalse(translator.IsVowel(' '))
        self.assertFalse(translator.IsVowel('-'))
        self.assertFalse(translator.IsVowel('1'))

    def test_Translate_singleword_initialvowel(self):
        self.assertEqual(translator.Translate("aardvark"), "aardvarkway")

    def test_Translate_singleword_initialconsonant(self):
        self.assertEqual(translator.Translate("foo"), "oofay")

    def test_Translate_singleword_uppercase(self):
        self.assertEqual(translator.Translate("Aardvark"), "Aardvarkway")
        self.assertEqual(translator.Translate("Foo"), "Oofay")

    def test_Translate_multiplewords(self):
        self.assertEqual(translator.Translate("this is a test"),
                         "isthay isway away esttay")
        self.assertEqual(translator.Translate("And this has Capital Letters."),
                         "Andway isthay ashay Apitalcay Etterslay.")

    def test_Translate_multiplelines(self):
        original = """Testing 1 2 3.
        Newline, newline!
        ...Is this thing on?"""
        expected = """Estingtay 1 2 3.
        Ewlinenay, ewlinenay!
        ...Isway isthay ingthay onway?"""

        self.assertEqual(translator.Translate(original), expected)

if __name__ == "main":
    unittest.main()
