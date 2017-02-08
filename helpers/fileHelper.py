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

    return open(textFiles[int(input("Enter a number: ")) - 1], mode, encoding=encoding)
