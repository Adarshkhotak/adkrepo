
"""
Time Complexity = O(n), n is number of elements in array
Space Complexity = O(1)

This code is actually similar to Brute force one
"""
#to LEFT side
'''
from typing import List
def rotateArray(arr:List, n: int):
    temp = arr[0]  # storing the first element of the array in a variable
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp  # assign the value of the variable at the last index
    return arr'''

#To RIGHT Side
from typing import List
def rotateArray(arr:List, n: int):
     
    return arr

print(rotateArray([1,2,3,4,5,6,7],7))
