"""Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.
Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65]."""

def count_positives_sum_negatives(lst):
    if not lst:
        return []
    pos, neg = 0,0
    for i in lst:
        if i <= 0:
            neg += i
        else:
            pos += 1
    return [pos,neg]
