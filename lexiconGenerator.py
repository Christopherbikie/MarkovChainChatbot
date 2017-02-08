import pickle

from helpers import fileHelper
from helpers import stringHelper

textFile = fileHelper.selectFile("texts", "txt")
text = []
for line in textFile:
    for word in line.split():
        text.append (word)
textFile.close()

successorList = {}

for word in list(set(text)):
    working = []
    for i in range(len(text) - 1):
        if word == text[i] and text[i][-1] not in "().?!":
            working.append(stringHelper.remChars(str(text[i + 1]), "()"))
    if len(working) > 0:
        successorList[word] = working

outFile = open(textFile.name[:-4] + ".lex", "wb")
pickle.dump(successorList, outFile, 2)
outFile.close()
