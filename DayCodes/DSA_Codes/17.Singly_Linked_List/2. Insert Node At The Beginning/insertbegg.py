class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


# Do not change code above.


def insertAtFirst(list: Node, newValue: int) -> Node:
    if list is None:
        new_head=Node(newValue)
    else:
        new_head=Node(newValue)
        new_head.next=list
    return new_head

#To insert at Start and End gfg
'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the beginning of the linked list.
    def insertAtBegining(self,head,x):
        new_node=Node(x)
        new_node.next=head
        return new_node
        
            
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        if head is None:
            return Node(x)
        curr=head
        while curr.next is not None:
            curr=curr.next
        
        curr.next=Node(x)
        return head