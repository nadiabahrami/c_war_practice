"""Given a positive integer n: 0 < n < 1e6, remove the last digit until you're left with a number that is a multiple of three.

Return n if the input is already a multiple of three, and return null/nil/None if no such number exists.
Examples

1      => null
25     => null
36     => 36
1244   => 12
952406 => 9

"""

def prev_mult_of_three(n):
    while n > 1:
        if n % 3 == 0:
            return n
        else: 
            n = n // 10
    return None