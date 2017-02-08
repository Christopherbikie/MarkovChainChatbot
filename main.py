import pickle
import random

from helpers import fileHelper


# TODO Select next word based on number of occurances rather than random
def nextWord(current, prev = None):
    if current is not None and (prev, current) in successorsFromPairs:
        return random.choice(successorsFromPairs[(prev, current)])
    elif current in successors:
        return random.choice(successors[current])
    else:
        return "the"


lexicon = fileHelper.selectFile("texts", "lex", "rb")
successors, successorsFromPairs = pickle.load(lexicon)
lexicon.close()

speech = ""

while speech != "quit":
    speech = input("> ")
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
