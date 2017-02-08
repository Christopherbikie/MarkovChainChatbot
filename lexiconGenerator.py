import pickle
from collections import defaultdict

from helpers import fileHelper
from helpers import stringHelper

textFile = fileHelper.selectFile("texts", "txt")
text = []
for line in textFile:
    for word in line.split():
        text.append (word)
textFile.close()

successors = {}

# TODO: speed this bit up
for word in list(set(text)):
    working = []

    for i in range(len(text) - 1):
        if word == text[i] and text[i][-1] not in "().?!":
            working.append(stringHelper.remChars(str(text[i + 1]), "()"))

    if len(working) > 0:
        successors[word] = working

successorsFromPairs = defaultdict(list)
for i in range(len(text) - 2):
    successorsFromPairs[(text[i], text[i + 1])].append(text[i+2])

outFile = open(textFile.name[:-4] + ".lex", "wb")
pickle.dump((successors, successorsFromPairs), outFile, 2)
outFile.close()
