"""
Time complexity = O(n) where n is the number of elements in list
But in this case, we are using only 1 loop instead of 2 FOR loops

Space complexity = O(1), no extra space
"""

def removeDuplicates(arr,n):
    i=0
    j=i+1
    while j<n:
        if arr[j]!=arr[i]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    return i+1

print(removeDuplicates([1, 2, 2,4, 2, 3],6))