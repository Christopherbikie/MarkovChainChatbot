import pickle
from collections import defaultdict

from helpers import inputHelper

textFile = inputHelper.selectFile("texts", "txt")
text = []
for line in textFile:
    for word in line.split():
        text.append(word)
textFile.close()

successors = defaultdict(list)
for i in range(len(text) - 1):
    successors[text[i].lower()].append(text[i + 1])

successorsFromPairs = defaultdict(list)
for i in range(len(text) - 2):
    successorsFromPairs[(text[i].lower(), text[i + 1].lower())].append(text[i + 2])

outFile = open(textFile.name[:-4] + ".lex", "wb")
pickle.dump((successors, successorsFromPairs), outFile, 2)
outFile.close()
