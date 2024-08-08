from sys import *
from collections import *
from math import *
from typing import List

def largestElement(arr:List, n: int) -> int:
    largest=arr[0]
    for i in range(0,n):
        if arr[i]>largest:
            largest=arr[i]
    return largest

print(largestElement([1, 2, 12, 4, 5],5))