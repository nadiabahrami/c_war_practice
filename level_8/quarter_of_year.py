"""Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.
Fundamentals"""
def quarter_of(month):
    return month // 3 if (month / 3).is_integer() else (month // 3) + 1

from math import ceil
def quarter_of_bp(month):
    return ceil(month / 3)