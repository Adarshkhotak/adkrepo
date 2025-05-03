#Coding-Ninja
'''TC=O(N(N-1))==O(N**2)
SC=O(1)'''
from typing import List

def nextGreaterElement(arr: List[int], n: int) -> List[int]:
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                arr[i]=arr[j]
                break
        else:
            arr[i]=-1
    return arr