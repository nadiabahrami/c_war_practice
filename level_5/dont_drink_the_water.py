"""Don't Drink the Water

Given a two-dimensional array representation of a glass of mixed liquids, sort the array such that the liquids appear in the glass based on their density. (Lower density floats to the top) The width of the glass will not change from top to bottom.

======================
|   Density Chart    |
======================
| Honey   | H | 1.36 |
| Water   | W | 1.00 |
| Alcohol | A | 0.87 |
| Oil     | O | 0.80 |
----------------------

[                            [
 ['H', 'H', 'W', 'O'],        ['O','O','O','O']
 ['W', 'W', 'O', 'W'],  =>    ['W','W','W','W']
 ['H', 'H', 'O', 'O']         ['H','H','H','H']
 ]                           ]
 

The glass representation may be larger or smaller. If a liquid doesn't fill a row, it floats to the top and to the left.
"""

def separate_liquids(glass):
    if not glass:
        return []
    dict = {"O":0, "A":0, "W":0, "H":0}
    row = len(glass[0])
    col = len(glass)
    for l in glass:
        for m in l:
            dict[m] += 1
    r = []
    result = []
    for i in range(row*col):
        if dict["O"] != 0:
            r.append("O")
            dict["O"] -= 1
        elif dict["A"] != 0:
            r.append("A")
            dict["A"] -= 1
        elif dict["W"] != 0:
            r.append("W")
            dict["W"] -= 1
        else:
            r.append("H")
            dict["H"] -= 1
        if len(r) == row:
            result.append(r)
            r = []
    return result