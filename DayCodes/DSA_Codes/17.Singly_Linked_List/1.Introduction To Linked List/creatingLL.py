class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Do not change code above.

from typing import List
def constructLL(arr: List[int]) -> Node:
    new_head=Node(arr[0])
    current_node=new_head
    for i in range(1,len(arr)):
        new_node=Node(arr[i])
        current_node.next=new_node
        current_node=new_node
    return new_head

'''The new_head variable keeps track of the head of the newly created linked list. Finally, the function returns new_head'''