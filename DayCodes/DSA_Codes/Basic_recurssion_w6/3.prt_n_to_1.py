from typing import List

def printNos(x: int) -> List[int]:
    if x==0:
        return
    
    print(x,end=" ")
    printNos(x-1)

printNos(5)