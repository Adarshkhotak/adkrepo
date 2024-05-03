from  typing import *

def printNtimes(n: int) -> List[str]:
    if n==0:
        return []
    print("Coding Ninjas")
    printNtimes(n-1)

printNtimes(4)