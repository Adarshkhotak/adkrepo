"""
Time Complexity = O(N), N is length of array
Space Complexity: O(1) it is reduced then brute
"""
from typing import List
def moveZeros(n: int,  a: List[int]):
    i,j=0,0
    while i<n and j<n:
        if a[j]==0:  #to find zero's in array
            j+=1
        else:
            a[i],a[j]=a[j],a[i]  #i,j same swipe eachother don't impact
            i+=1
            j+=1
    return a

print(moveZeros(6,[1, 2, 0, 0, 2, 3]))        
