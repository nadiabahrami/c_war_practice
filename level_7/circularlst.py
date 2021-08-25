"""Create a Circular List

A circular list is of finite size, but can infititely be asked for its previous and next elements. This is because it acts like it is joined at the ends and loops around.

For example, imagine a CircularList of [1, 2, 3, 4]. Five invocations of next() in a row should return 1, 2, 3, 4 and then 1 again. At this point, five invocations of prev() in a row should return 4, 3, 2, 1 and then 4 again.

Your CircularList is created by passing a vargargs parameter in, e.g. new CircularList(1, 2, 3). Your list constructor/init code should throw an Exception if nothing is passed in.
Fundamentals
Lists
Data Structures"""

class CircularList():
    def __init__(self, *args):
        if args:
            self.lst = args
            self.i = -1
        else: raise Exception("Arguemnts can't be empty")
        
    def next(self):
        if self.i < len(self.lst)-1:
            self.i += 1
        else:
            self.i = 0
        return self.lst[self.i]
        
    def prev(self):
        if self.i <= 0:
            self.i = len(self.lst) - 1
        else:
            self.i -= 1
        return self.lst[self.i]