class Translator():

    def __init__(self):
        self.inWord = False

    def Translate(self, text):
        """Translate the given text into Pig Latin

        Based on the (simple) rules at
        https://en.wikipedia.org/wiki/Pig_Latin#Rules.
        """

        return self.TranslateWord(text)

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

        return translation

    @classmethod
    def IsVowel(self, char):
        return char and char.lower() in "aeiouy"
