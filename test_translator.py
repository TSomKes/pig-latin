#!/usr/bin/env python3


import unittest

import translator


class TestTranslator(unittest.TestCase):

    def test_FindSplit_wordsimple(self):
        self.assertEqual(translator.FindSplit('a'), 0)
        self.assertEqual(translator.FindSplit('b'), 1)
        self.assertEqual(translator.FindSplit('test'), 1)
        self.assertEqual(translator.FindSplit('know'), 2)

    def test_FindSplit_wordcontains_y(self):
        self.assertEqual(translator.FindSplit('try'), 2)
        self.assertEqual(translator.FindSplit('chrysalis'), 3)
        self.assertEqual(translator.FindSplit('yes'), 1)
        self.assertEqual(translator.FindSplit('Yvonne'), 0)

    def test_FindSplit_wordcontains_qu(self):
        self.assertEqual(translator.FindSplit('quit'), 2)
        self.assertEqual(translator.FindSplit('squishy'), 3)

    def test_FindSplit_nonword(self):
        self.assertEqual(translator.FindSplit(''), 0)
        self.assertEqual(translator.FindSplit(' '), 1)
        self.assertEqual(translator.FindSplit('-'), 1)
        self.assertEqual(translator.FindSplit('1'), 1)
        self.assertEqual(translator.FindSplit('...)?", '), 8)

    def test_Translate_singleword_initialvowel(self):
        self.assertEqual(translator.Translate("aardvark"), "aardvarkway")

    def test_Translate_singleword_initialconsonant(self):
        self.assertEqual(translator.Translate("foo"), "oofay")

    def test_Translate_singleword_uppercase(self):
        self.assertEqual(translator.Translate("Aardvark"), "Aardvarkway")
        self.assertEqual(translator.Translate("Foo"), "Oofay")

    def test_Translate_singleword_apostrophes(self):
        self.assertEqual(translator.Translate("don't"), "on'tday")
        self.assertEqual(translator.Translate("Peter's"), "Eter'spay")

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
