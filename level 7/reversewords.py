"""Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
Examples

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""

def reverse_words(text):
    lst = text.split(" ")
    for i,v in enumerate(lst):
        lst[i] = "".join(reversed(v))
    return " ".join(lst)

def reverse_words_bp(str):
    return ' '.join(s[::-1] for s in str.split(' '))    
