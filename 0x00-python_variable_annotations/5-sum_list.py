#!/usr/bin/env python3
"""Complex types - list of floats
Write type-annotated function sum_list, takes input_list of floats
as arguments
Returns their sum as float"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """which takes a list input_list of
    floats as argument and returns their sum as a float.
    """
    sum = 0
    for i in input_list:
        if type(i) == float:
            sum += i
    return sum
