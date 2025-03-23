'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def length(head) :
    current=head
    count=0
    while current:
        count+=1
        current=current.next
    return count