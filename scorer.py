import copy

from helpers import stringHelper

replace = {
    "my": "your",
    "your": "my",
    "i": "you",
    "you": "I",
    "why": "because",
    "this": "that",
    "whats": "is",
    "what's": "is",
}
remove = [
    "the",
    "a",
    "an",
    "and",
    "what",
    "when",
    "where",
    "that",
]


def processInput(input):
    for i in range(len(input)):
        input[i] = stringHelper.remChars(input[i], ".,!?")

    for i in range(len(input) - 1, -1, -1):
        word = stringHelper.remChars(input[i], ".,!?")
        if word in remove:
            del input[i]
        elif word in replace:
            input[i] = replace[word]


def getScore(input: list, question: bool, response: list):
    input = copy.deepcopy(input)

    score = 0
    if question and response[-1][-1] == "?":
        score -= 1

    countedWords = []
    for word in response:
        word = word.lower()
        if word in input and word not in countedWords:
            score += 1
            countedWords.append(word)

    if len(response) >= 10:
        score = score - 1.15 ** (len(response) - 10) + 1
    if len(response) <= 3:
        score -= 1

    return score
