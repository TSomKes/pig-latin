from itertools import takewhile


def Translate(text):
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
            translation += TranslateWord(chunk)
        else:
            chunk = ''.join(takewhile(lambda c: not c.isalpha(),
                            remaining))
            translation += chunk

        # Lop off the chunk we just processed
        remaining = remaining[len(chunk):]

    return translation


def TranslateWord(word):

    translation = ""

    split = FindSplit(word)

    translation = word[split:] + word[:split]

    if split > 0:
        translation += "ay"
    else:
        translation += "way"

    # We only support capital letters at the beginning of the word.  Stomp
    # all the rest down to lower-case, and then condtionally captialize the
    # "new" first letter.
    translation = translation.lower()
    if word[0].isupper():
        translation = translation[0].upper() + translation[1:]

    return translation


# Find the "split" point in a word--basically, the first vowely-vowel.  
# Assumes we've been handed a well-formed word.  
def FindSplit(word):

    i = 0
    while i < len(word):
        # Split at the first vowel found...
        if word[i].lower() in "aeio":
            break
        # ...unless that first vowel happens to be a U following a Q.
        elif word[i].lower() == 'u':
            if word[i-1].lower() != 'q':
                break
        # Initial Ys are only considered vowels when not followed by another
        # vowel.
        elif word[i].lower() == 'y':
            if i != 0 or word[i + 1].lower() not in "aeiou":
                break

        i += 1

    return i 
