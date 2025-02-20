#Just find out index of minimum value
from typing import List
def findKRotation(arr :List [int]) -> int:
    n = len(arr)
    low = 0
    high = n - 1
    index=-1
    minimum = float("inf")
    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[mid]:
            if arr[low]<minimum:
                minimum=arr[low]
                index=low
            low=mid+1
        else:
            if arr[mid]<minimum:
                minimum=arr[mid]
                index=mid
            high=mid-1
    return index
