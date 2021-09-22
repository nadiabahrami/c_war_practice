"""Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""

def high(x):
    lst = x.split(" ")
    max = (0, "")
    for word in lst:
        sum = 0
        for c in word:
            sum += (ord(c) - 96)
        if sum > max[0]:
            max = (sum, word)
    return max[1]

def high_bp(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))