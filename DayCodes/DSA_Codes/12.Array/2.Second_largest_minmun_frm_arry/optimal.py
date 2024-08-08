"""
We are using 1 loop only, so TC will be O(N).

Time complexity = O(N) where N is the number of elements in list
Space complexity = O(1)
"""
from  typing import List
def getSecondOrderElements(n: int,  a:List):
    small=float("inf")
    large=float("-inf")
    sec_small=float("inf")
    sec_large=float("-inf")

    for i in range(0,n):
        if a[i]>large:
            sec_large=large
            large=a[i]
        elif a[i]>sec_large and a[i]!=large: #this if numbers is between large and sec_large
            sec_large=a[i]

        if a[i]<small:
            sec_small=small
            small=a[i]
        elif a[i]< sec_small and a[i]!=small:
            sec_small=a[i]

    return[sec_large,sec_small]  

print(getSecondOrderElements(5, [1, 2, 3, 4, 5])) 