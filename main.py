import pickle
import random

from helpers import inputHelper


def nextWord(current, prev = None):
    current = current.lower()
    if prev is not None and (prev.lower(), current) in chainOrder2:
        return chainOrder2[(prev.lower(), current)].next()
    elif current in chainOrder1:
        return chainOrder1[current].next()
    else:
        return "the"


lexicon = inputHelper.selectFile("texts", "lex", "rb")
chainOrder1, chainOrder2 = pickle.load(lexicon)
lexicon.close()

speech = ""

while speech != "quit":
    speech = inputHelper.getString("> ")
    # noinspection PyRedeclaration
    currentWord = random.choice(speech.split())
    response = [currentWord]

    while True:
        if len(response) > 1:
            newWord = nextWord(currentWord, response[-2])
        else:
            newWord = nextWord(currentWord)
        response.append(newWord)
        currentWord = newWord
        if newWord[-1] in "?!.":
            break

    print(" ".join(response))
