from typing import List
def isSorted(n: int,  a: List) -> int:
    i=0
    while i<n-1:
        if a[i]<=a[i+1]:
            i+=1
        else:
            return 0
    return 1

print(isSorted(5,[1, 2, 3, 4, 5]))