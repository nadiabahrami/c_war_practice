"""Write a function that returns a string in which firstname is swapped with last name.

name_shuffler('john McClane'); => "McClane john"
"""
def name_shuffler(str_):
    return str_.split()[1] + ' ' + str_.split()[0]


def name_shuffler_bp(str_):
    return ' '.join(str_.split(' ')[::-1])