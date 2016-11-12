#!/usr/bin/env python3


import os

from translator import Translate


messageWelcome = "Pig Latin"
messageGoodbye = "Goodbye! :)"


# Clear display
os.system('cls')
os.system('clear')

# Print welcome message
print(messageWelcome + ":  " + Translate(messageWelcome))
print("\nTo finish translating, enter 'quit'.\n")

done = False
while not done:
    text = input("Text to translate: ")
    done = text.lower() in ['quit', 'itquay']   # User quitting?
    print(Translate(text) + '\n')

print(Translate(messageGoodbye))
