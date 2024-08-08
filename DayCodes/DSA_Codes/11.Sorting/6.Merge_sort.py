from typing import List
def mergeSort(arr:List[int]):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]
    LH=mergeSort(left_half)
    RH=mergeSort(right_half)
    return merge(LH,RH)

def merge(left,right):
    merged=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    while i<len(left):
        merged.append(left[i])
        i+=1
    while j<len(right):
        merged.append(right[j])
        j+=1

    return merged

print(mergeSort([2, 13, 4, 1, 3, 6, 28]))