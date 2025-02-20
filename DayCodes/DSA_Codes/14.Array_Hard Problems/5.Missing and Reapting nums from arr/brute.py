'''TC=O(N**2)
   SC=O(1)'''

from typing import List
def findMissingRepeatingNumbers(a: List[int]) -> List[int]:
    n=len(a)
    rep=-1
    mis=-1
    for i in range(1,n+1):
        count=0
        for j in range(0,n):
            if a[j]==i:
                count+=1
        
        if count==2:
            rep=i
        elif count==0:
            mis=i
        if rep!=-1 and mis !=-1:
            break
    return [rep,mis]