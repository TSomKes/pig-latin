#!/usr/bin/env python3


import os

import translator


messageWelcome = "Pig Latin"
messageGoodbye = "Goodbye! :)"


t = translator.Translator()

# Clear display
os.system('cls')
os.system('clear')

# Print welcome message
print(messageWelcome + ":  " + t.Translate(messageWelcome))
print(""" 
To finish translating, enter 'quit'.
""")

done = False
while not done:
    text = input("Text to translate: ")
    done = text in ['quit', 'itquay']   # User quitting?
    print(t.Translate(text) + '\n')

print(t.Translate(messageGoodbye))
