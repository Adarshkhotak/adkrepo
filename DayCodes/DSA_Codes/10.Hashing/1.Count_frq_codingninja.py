from typing import List

def countFrequency(n: int, m: int, edges: List[List[int]]):

    mylst = [0] * n
    #print(mylst)

    for x in edges:
        if x > n:
            continue
        #print(x-1)
        mylst[x - 1] += 1 #x-1 coz they want 
# 0 represents the frequency of 1, index 1 represents the frequency of 2, and so on.
    return mylst


print(countFrequency(6, 9, [1, 3, 1, 9, 2, 7]))