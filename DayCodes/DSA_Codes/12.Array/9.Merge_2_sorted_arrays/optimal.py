"""
Time complexity -> O(n+m)
n is number of elements in a
m is number of elements in b

Space complexity -> O(1) res[] is the so we don;t take this as space
"""
from typing import List
def sortedArray(a: List[int], b: List[int]) ->List [int]:
    # Write your code here
    res=[]
    i,j=0,0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            if len(res)==0 or res[-1]!=a[i]: #want uniqe result not like merge
                res.append(a[i])
            i+=1
        else:   
            if len(res)==0 or res[-1]!=b[j]:
                res.append(b[j])
            j+=1
    
    while i<len(a):
        if len(res)==0 or res[-1]!=a[i]:
            res.append(a[i])
        i+=1
    while j<len(b):
        if len(res)==0 or res[-1]!=b[j]:
            res.append(b[j])
        j+=1

    return res

print(sortedArray([1, 2, 3, 4, 6],[2, 3, 5]))