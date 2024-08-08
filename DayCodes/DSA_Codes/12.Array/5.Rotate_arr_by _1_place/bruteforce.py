"""
Time Complexity = O(n), n is number of elements in array
Space Complexity = O(1)
"""
from typing import List

def rotateArray(arr:List, n: int):
    last_element = arr.pop(0)
    arr.append(last_element)
    return arr