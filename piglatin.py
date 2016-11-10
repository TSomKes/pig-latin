#!/usr/bin/env python3


import os

import translator


t = translator.Translator()

# Clear display
os.system('cls')
os.system('clear')

# Print welcome message
print("""Pig Latin:  Igpay Atinlay

To finish translating, enter 'quit'.
""")

done = False
while not done:
    text = input("Text to translate: ")
    done = text in ['quit', 'itquay']   # User quitting?
    print(t.Translate(text) + '\n')

print("Oodbyegay")
