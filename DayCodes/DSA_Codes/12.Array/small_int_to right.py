def small_int_rightside(arr):
    res=[-1]*len(arr)
    min_so_far=float('inf')
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>min_so_far:
            res[i]=min_so_far
        min_so_far=min(min_so_far,arr[i])
    return res
        

print(small_int_rightside([2,4,8,3,5,9]))