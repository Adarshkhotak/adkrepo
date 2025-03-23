class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next


# Please do not change code above.


def insertAtTail(head: Node, k: int) -> Node:
    new_node=Node(k)
    if head is None :
        head=new_node
        return head #Here shilud be return
    temp=head
    while temp.next:
        temp=temp.next
    temp.next=new_node
    new_node.prev=temp
    return head