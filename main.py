import pickle
import random

import scorer
from helpers import inputHelper


def getResponse(input):
    input = input.split(" ")
    bestResponse = ""
    bestScore = 0

    for i in range(10000):
        # noinspection PyRedeclaration
        # currentWord = random.choice(input)
        # currentWord = "My"
        currentWord = random.choice(["My", "The", "When", "I", "What"])
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
        score = scorer.getScore(input, response)
        if score > bestScore:
            bestResponse = response
            bestScore = score
        # if "name" in response:
        #     print(str(score) + " ".join(response))

    print(bestScore)
    return bestResponse


def nextWord(current, prev=None):
    current = current.lower()
    if prev is not None and (prev.lower(), current) in chainOrder2:
        return chainOrder2[(prev.lower(), current)].next()
    if current in chainOrder1:
        return chainOrder1[current].next()
    else:
        return "the"


lexicon = inputHelper.selectFile("texts", "lex", "rb")
chainOrder1, chainOrder2 = pickle.load(lexicon)
lexicon.close()

speech = ""

while speech != "quit":
    speech = inputHelper.getString("> ")

    print(" ".join(getResponse(speech)))
