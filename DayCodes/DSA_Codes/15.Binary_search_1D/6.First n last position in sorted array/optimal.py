'''
TC=O(2 log N)==log N
SC=O(1)'''
def BinarySearchLeft(arr,n,k):
    l=0
    h=n-1
    inx=-1
    while l<=h:
        m=(l+h)//2
        if arr[m]==k:
            inx=m
            h=m-1
        elif arr[m]>k:
            h=m-1
        else:
            l=m+1
    return inx

def BinarySearchRight(arr,n,k):
    l=0
    h=n-1
    inx=-1
    while l<=h:
        m=(l+h)//2
        if arr[m]==k:
            inx=m
            l=m+1
        elif arr[m]>k:
            h=m-1
        else:
            l=m+1
    return inx

def firstAndLastPosition(arr, n, k):
    Left=BinarySearchLeft(arr,n,k)
    Right=BinarySearchRight(arr,n,k)

    return Left,Right