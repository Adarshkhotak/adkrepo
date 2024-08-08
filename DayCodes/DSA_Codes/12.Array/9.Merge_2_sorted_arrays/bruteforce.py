"""
Time complexity -> O((n + m) log (n + m))
n is number of elements in a
m is number of elements in b

Space complexity -> O(n+m)
"""

from typing import List
def sortedArray(a: List[int], b: List[int]) -> List[int]:
    freq = set()

    for num in a:
        freq.add(num)
    for num in b:
        freq.add(num)

    return sorted(list(freq))

print(sortedArray([1, 2, 3, 4, 6],[2, 3, 5]))