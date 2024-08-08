from typing import List

def bubbleSort(arr: List[int], n: int):
    for i in range(n-2,-1,-1): #n-2 coz we want to start i from 2nd last elemnet
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(bubbleSort([2, 13, 4, 1, 3, 6, 28],7))
