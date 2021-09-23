"""Task

An employee wishes to resign. Do not let him go.

Locate the entrance to his office so we can send its coordinates to the orbital obstacle placement service (OOPS).

The floor plan of the office is given as a list of strings. Walls are marked with a # and interior with .. Strings can vary in length, and if they do, align them to the left.

Return the coordinates of the office entrance as a tuple (x, y). Top left is (0, 0), x is oriented to the right ("columns") and y downwards ("rows"):

+----> x
|
|
V
y

Examples

###.###
#.....#
#.....#  ->  (3, 0)
#....##
######

 #####
 #...#
 ....#
 #...#  ->  (1, 2)
##...#
#....#
######

"""
def locate_entrance(office: List[str]) -> Tuple[int, int]:
    for y, v in enumerate(office):
        for x, s in enumerate(list(v)):
            print((x,y,s,v))
            if s == ".":
                if x == 0 or y == 0:
                    return (x, y)
                try:
                    if office[y][x-1] == " " or office[y][x+1] == " " or office[y-1][x] == " " or office [y+1][x] == " ":
                        return (x, y)
                except IndexError:
                    return (x, y)
