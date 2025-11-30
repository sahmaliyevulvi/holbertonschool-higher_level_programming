#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
        }
    if isinstance(roman_string, int) or roman_string is None:
        return 0
    a = 0
    r = 0
    n = len(roman_string)
    while a < n:
        if a + 1 < n and roman_string[a: a+2] in dic:
            r += dic[roman_string[a: a+2]]
            a += 2
        else:
            r += dic[roman_string[a]]
            a += 1
    return r
