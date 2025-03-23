from typing import List
'''TC=O(N**2)
sc=O(1)'''

def subarrayWithSum(arr: List[int], k: int) -> int:
    count=0
    n=len(arr)
    for i in range(0,n):
        sum=0
        for j in range(i,n):
            sum=sum+arr[j]
            if sum==k:
                count+=1

            if sum > k: #if k=2 n subarry is 0,1,0,1,0,0 i.w we can't stop at 1 nxt need to be move as 0,0 sum remains same.
                break
    return count