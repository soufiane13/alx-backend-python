#!/usr/bin/env python3
"""
Define
script for  a type-annotated function
which takes a list mxd_lst of integers and floats
and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Typed-annotated function
    sum_mixed_list
    """
    return sum(mxd_lst)
