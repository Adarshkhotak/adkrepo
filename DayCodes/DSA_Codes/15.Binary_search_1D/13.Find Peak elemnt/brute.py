from typing import List
"""
Time complexity -> O(N)
Here, N = size of the given array.

Space complexity -> O(1)
"""

def findPeakElement(arr:List [int]) -> int:
    n=len(arr)
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1
    for i in range(1,n-1):
        if arr[i]>arr[i+1] and arr[i]>arr[i-1]:
            return i

print(findPeakElement([1,2,1,3,5,6,4]))

#Explanation: Your function can return either index number 1 where the peak element is 2,
# or index number 5 where the peak element is 6.