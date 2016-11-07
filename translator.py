class Translator():

    def __init__(self):
        self.outputText = ""
        self.stagedConsonants = ""
        self.foundVowel = False

    def Translate(self, text):
        for c in text:
            if self.foundVowel:
                self.outputText += c
            else:
                if Translator.IsVowel(c):
                    self.foundVowel = True
                    self.outputText += c
                else:
                    self.stagedConsonants += c

        if self.stagedConsonants:
            self.outputText += self.stagedConsonants + "ay"
        else:
            self.outputText += "way"

        return self.outputText

    @classmethod
    def IsVowel(self, char):
        return char and char.lower() in "aeiouy"
