from typing import *

def getSingleElement(arr : List[int]) -> int:
    # Write your code here.
    my_dict={}
    for i in range(len(arr)):
        my_dict[arr[i]]=my_dict.get(arr[i],0)+1
    
    for k,v in my_dict.items():
        if v==1:
            return k


print(getSingleElement([1, 1, 2, 3, 3, 4, 4]))