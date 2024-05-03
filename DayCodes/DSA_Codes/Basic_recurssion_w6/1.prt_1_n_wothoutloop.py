'''
from typing import List

def printNos(x:int)->List[int]:
   
    if x<1:
        return
    printNos(x-1)
    print(x,end=" ")

printNos(5)'''

from typing import List

def printNos(x: int) -> List[int]:
    ls=[]
    if x==0:
        return
    printNos(x-1)
    ls.append(x)
    return ls

a=printNos(5)
print(a)
