import glob
import os


def selectFile(path, extention, mode = "r"):
    print("Detected file(s):")
    textFiles = glob.glob(os.path.join(path, "*." + extention))
    for i in range(len(textFiles)):
        print(str(i + 1) + ": " + textFiles[i][6:])

    if mode == "":
        mode = "r"

    encoding = None
    if not "b" in mode:
        encoding = "utf8"

    fileIndex = getChar("Enter a number: ", "".join(str(i) for i in range(1, len(textFiles) + 1)))
    return open(textFiles[int(fileIndex) - 1], mode, encoding=encoding)


def getChar(text, valid):
    while True:
        userInput = input(text)
        if len(userInput) == 1 and userInput in valid:
            break
    return userInput


def getString(text):
    while True:
        userInput = input(text)
        if len(userInput) > 0:
            break
    return userInput
