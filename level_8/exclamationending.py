"""Description:

Remove all exclamation marks from the end of sentence.
Examples

remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi! Hi"
remove("Hi") === "Hi"

"""

def remove(s):
    while s and s[-1] == "!":
        s = s[:-1]
    return s
    

def remove_bp(s):
     return s.rstrip("!")
