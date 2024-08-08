def insertionSort(arr):
    
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]<key: #only taken '<'
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
    return arr

print(insertionSort([2, 13, 4, 1, 3, 6, 28]))