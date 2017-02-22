replace = {
    "my": "your",
    "your": "my",
    "i": "you",
    "you": "I",
    "why": "because",
    "this": "that"
}
remove = [
    "i",
    "the",
    "a",
    "an",
    "and",
    "what",
    "when",
]


def getScore(input: list, response: list):
    for i in range(len(input)):
        input[i] = input[i].lower()
    for i in range(len(response)):
        response[i] = response[i].lower()

    score = 0
    for i in range(len(input) - 1, -1, -1):
        word = input[i]
        if word in remove:
            del input[i]
        elif word in replace:
            input[i] = replace[word]

    countedWords = []
    for word in response:
        if word in input and word not in countedWords:
            score += 1
            countedWords.append(word)

    if len(response) > 10:
        score = score - 1.15 ** (len(response) - 10) + 1

    return max(score, 0)
