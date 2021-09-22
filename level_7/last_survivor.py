"""
You are given a string of letters and an array of numbers.
The numbers indicate positions of letters that must be removed, in order, starting from the beginning of the array.
After each removal the size of the string decreases (there is no empty space).
Return the only letter left.

Example:

let str = "zbk", arr = [0, 1]
    str = "bk", arr = [1]
    str = "b", arr = []
    return 'b'

Notes

    The given string will never be empty.
    The length of the array is always one less than the length of the string.
    All numbers are valid.
    There can be duplicate letters and numbers.

If you like this kata, check out the next one: Last Survivors Ep.2
"""

def last_survivor(letters, coords):
    if not coords:
        return letters
    ltr = list(letters)
    for i in coords:
        del ltr[i]
    return "".join(ltr)

def last_survivor(letters, coords):
    for x in coords:
        letters = letters[0:x] + letters[x+1:]
    return letters
