def SecondLargMin(arr):
    arr.sort()
    return [arr[1],arr[-2]]

print(SecondLargMin([1, 4,8,6, 3, 4, 5,2]))