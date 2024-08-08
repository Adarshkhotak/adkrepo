"""
We are using 2 for loops, so it will be O(N) + O(N).
Which will be equal to O(2N)
Which then comes down to O(N)

Time complexity = O(N) where N is the number of elements in list
Space complexity = O(1)
"""

from typing import List
def getSecondOrderElements(n: int,  a: List):
    small=float("inf")
    large=float("-inf")
    sec_small=float("inf")
    sec_large=float("-inf")

    for i in range(0,n):
        small=min(small,a[i])
        large=max(large,a[i])
    
    for i in range(0,n):
        if a[i]<sec_small and a[i]!=small:
            sec_small=a[i]

        if a[i]>sec_large and a[i]!=large:
            sec_large=a[i]

    return[sec_large,sec_small] 

print(getSecondOrderElements(5, [1, 2, 3, 4, 5]))  