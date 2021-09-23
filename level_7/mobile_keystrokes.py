"""Do you remember the old mobile display keyboards? Do you also remember how inconvenient it was to write on it?
Well, here you have to calculate how much keystrokes you have to do for a specific word.

This is the layout:

Return the amount of keystrokes of input str (! only letters, digits and special characters in lowercase included in layout without whitespaces !)
Examples

mobileKeyboard("*#") => 2 (1+1)
mobileKeyboard("123") => 3 (1+1+1)
mobileKeyboard("abc") => 9 (2+3+4)
mobileKeyboard("codewars") => 26 (4+4+2+3+2+2+4+5)

"""

def mobile_keyboard(s):
    v = {3: set(['b', 'e', 'h', 'k', 'n', 'q', 'u', 'x']),
         4: set(['c', 'f', 'i', 'l', 'o', 'r', 'v', 'y']),
         5: set(['s', 'z'])}
    strokes = 0
    for c in s:
        if c in v[3]:
            strokes += 3
        elif c in v[4]:
            strokes += 4
        elif c in v[5]:
            strokes += 5
        elif c.isalpha():
            strokes += 2
        else:
            strokes += 1
    return strokes
        