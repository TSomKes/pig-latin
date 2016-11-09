from itertools import takewhile


class Translator():

    def __init__(self):
        pass

    def Translate(self, text):
        """Translate the given text into Pig Latin

        Based on the (very simple) rules at
        https://en.wikipedia.org/wiki/Pig_Latin#Rules.

        Note:
        - Supports initial capital letters only; assumes all others are
          lower-case.
        """

        translation = ""

        remaining = text

        # Find "chunks" of contiguous letters (words) or non-letters
        # (whitespace, punctuation)
        while remaining:

            chunk = ''
            if remaining[0].isalpha():
                chunk = ''.join(takewhile(lambda c: c.isalpha(), remaining))
                translation += self.TranslateWord(chunk)
            else:
                chunk = ''.join(takewhile(lambda c: not c.isalpha(),
                                remaining))
                translation += chunk

            # Lop off the chunk we just processed
            remaining = remaining[len(chunk):]

        return translation

    @classmethod
    def TranslateWord(self, text):

        translation = ""

        stagedConsonants = ""
        foundVowel = False

        for c in text:
            if foundVowel:
                translation += c
            else:
                if Translator.IsVowel(c):
                    foundVowel = True
                    translation += c
                else:
                    stagedConsonants += c

        if stagedConsonants:
            translation += stagedConsonants + "ay"
        else:
            translation += "way"

        # We only support capital letters at the beginning of the word.  Stomp
        # all the rest down to lower-case, and then condtionally captialize the
        # "new" first letter.
        translation = translation.lower()
        if text[0].isupper():
            translation = translation[0].upper() + translation[1:]

        return translation

    @classmethod
    def IsVowel(self, char):
        return char and char.lower() in "aeiouy"
