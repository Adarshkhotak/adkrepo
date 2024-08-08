'''TC=O(N) ,SC=O(1)'''
from typing import List
def linearSearch(n: int, num: int, arr: List[int]) -> int:
    for i in range(0,n):
        if arr[i]==num:
            return i
    return -1


#we hv method also arr.index(4)