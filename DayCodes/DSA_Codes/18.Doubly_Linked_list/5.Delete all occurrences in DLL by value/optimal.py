
class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


"""
Time complexity -> O(N)
N is the number of nodes

Space complexity -> O(1)
"""
def deleteAllOccurrences(head: Node, k: int) -> Node:
    if not head.next and head.data == k: #if not given this condition then also ok
        return None
    temp = head
    previous = None
    new_head = head
    while temp is not None:
        front = temp.next
        if temp.data == k:
            if previous is not None:
                previous.next = temp.next
            if temp.next:
                temp.next.prev = previous
            if temp == new_head:  #if by head.val== val
                new_head = new_head.next
        previous = temp
        temp = front
    return new_head

#OR
def deleteAllOccurrences(head: Node, k: int) -> Node:
    while head is not None and head.data == k:
        next_node=head.next
        if next_node:
            next_node.prev=None
        head=head.next
    temp = head
    previous = None
    while temp is not None:
        if temp.data == k:
            if previous is not None:
                previous.next = temp.next
            if temp.next:
                temp.next.prev = previous
        previous = temp
        temp = temp.next
    return head
