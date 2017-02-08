import pickle
from collections import defaultdict

import state
from helpers import inputHelper

textFile = inputHelper.selectFile("texts", "txt")
text = []
for line in textFile:
    for word in line.split():
        text.append(word)
textFile.close()

# current (str) -> state
chainOrder1 = defaultdict(state.State)
for i in range(len(text) - 1):
    chainOrder1[text[i].lower()].addTransition(text[i + 1])

chainOrder2 = defaultdict(state.State)
for i in range(len(text) - 2):
    chainOrder2[(text[i].lower(), text[i + 1].lower())].addTransition(text[i + 2])

outFile = open(textFile.name[:-4] + ".lex", "wb")
pickle.dump((chainOrder1, chainOrder2), outFile, 2)
outFile.close()
