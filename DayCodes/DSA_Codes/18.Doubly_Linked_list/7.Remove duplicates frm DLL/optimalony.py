
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


def removeDuplicates(head: Node) -> Node:
    temp = head
    while temp.next:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
            #temp.next.next.prev=temp not satisfey if last num are continous same 1 2 3 3 3
        else: #imp is same continues 12223
            temp = temp.next
    return head
