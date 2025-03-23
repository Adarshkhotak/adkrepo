class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class Solution:
    def delete_node(self, head, x):
        temp=head
        if x==1:
            head=head.next
            head.prev=None
        else:
    
            for _ in range(x-1):
                temp=temp.next
            
            if temp.next:
                temp.next.prev=temp.prev
            if temp.prev:
                temp.prev.next=temp.next #(basically it is  NOne)
        return head