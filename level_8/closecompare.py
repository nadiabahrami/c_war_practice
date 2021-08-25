"""Create a function close_compare that accepts 3 parameters: a, b, and an optional margin. The function should return whether a is lower than, close to, or higher than b.

a is considered "close to" b if margin is greater than or equal to the distance between a and b.

Please note the following:

    When a is close to b, return 0.

Otherwise...

    When a is less than b, return -1.

    When a is greater than b, return 1.

If margin is not given, treat it as zero.

Assume: margin >= 0

Tip: Some languages have a way to make parameters optional."""

def close_compare(a, b, margin=0):
    if a < (b-margin):
        return -1
    elif a > (b+margin):
        return +1
    return 0

def close_compare_bp(a,b,c=0):
    return 0 if abs(a - b) <= c else -1 if b > a else 1
