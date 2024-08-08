from typing import List
def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>pivot and j>=low-1:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j

def quickSort(arr: List[int], startIndex: int, endIndex: int):
    if startIndex<endIndex:
        pivot=partition(arr,startIndex,endIndex)
        quickSort(arr,startIndex,pivot-1)
        quickSort(arr,pivot+1,endIndex)
        return arr


print(quickSort([2, 13, 4, 1, 3, 6, 28],2,6))