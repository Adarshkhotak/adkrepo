

from typing import List
'''TC=O(2N)
    SC=O(1)'''
def findMissingRepeatingNumbers(a: List[int]) -> List[int]:
    n=len(a)
    hash_list=[0]*(n+1)
    for num in a:
        hash_list[num]+=1
    rep=-1
    mis=-1
    for i in range(1,len(hash_list)):
        if hash_list[i]==2:
            rep=i
        elif hash_list[i]==0:
            mis=i

        if rep!=-1 and mis!=-1:
            break
    return [rep,mis]
