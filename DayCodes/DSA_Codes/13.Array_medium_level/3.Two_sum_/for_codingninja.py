from typing import List
def read(n: int, book:List [int], target: int) -> str:
    # Write your code here.
    sum_dict=dict()
    for i in range(0,len(book)):
        rem=target-book[i]
        if rem in sum_dict:
            return 'YES'
        sum_dict[book[i]]=i
    return 'NO'