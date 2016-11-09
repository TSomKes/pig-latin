#!/usr/bin/env python3


import unittest

from translator import Translator


class TestTranslator(unittest.TestCase):

    def setUp(self):
        self.t = Translator()

    def test_IsVowel_vowels(self):
        self.assertTrue(self.t.IsVowel('a'))
        self.assertTrue(self.t.IsVowel('A'))

    def test_IsVowel_consonants(self):
        self.assertFalse(self.t.IsVowel('b'))
        self.assertFalse(self.t.IsVowel('B'))

    def test_IsVowel_empty(self):
        self.assertFalse(self.t.IsVowel(''))

    def test_IsVowel_nonalpha(self):
        self.assertFalse(self.t.IsVowel(' '))
        self.assertFalse(self.t.IsVowel('-'))
        self.assertFalse(self.t.IsVowel('1'))

    def test_Translate_singleword_initialvowel(self):
        self.assertEqual(self.t.Translate("aardvark"), "aardvarkway")

    def test_Translate_singleword_initialconsonant(self):
        self.assertEqual(self.t.Translate("foo"), "oofay")

    def test_Translate_singleword_uppercase(self):
        self.assertEqual(self.t.Translate("Aardvark"), "Aardvarkway")
        self.assertEqual(self.t.Translate("Foo"), "Oofay")

    def test_Translate_multiplewords(self):
        self.assertEqual(self.t.Translate("this is a test"),
                         "isthay isway away esttay")
        self.assertEqual(self.t.Translate("And this one has Capital Letters."),
                         "Andway isthay oneway ashay Apitalcay Etterslay.")

    def test_Translate_multiplelines(self):
        original = """Testing 1 2 3.
        Newline, newline!
        ...Is this thing on?"""
        expected = """Estingtay 1 2 3.
        Ewlinenay, ewlinenay!
        ...Isway isthay ingthay onway?"""

        self.assertEqual(self.t.Translate(original), expected)

if __name__ == "main":
    unittest.main()
