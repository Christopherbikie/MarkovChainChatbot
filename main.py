import pickle
import random

from helpers import fileHelper


def nextWord(a):
    if a in successorList:
        return random.choice(successorList[a])
    else:
        return "the"


lexicon = fileHelper.selectFile("texts", "lex", "rb")
successorList = pickle.load(lexicon)
lexicon.close()

speech = ""

while speech != "quit":
    speech = input("> ")
    # noinspection PyRedeclaration
    currentWord = random.choice(speech.split())
    response = currentWord

    while True:
        newWord = nextWord(currentWord)
        response += " " + newWord
        currentWord = newWord
        if newWord[-1] in "?!.":
            break

    print(response)
