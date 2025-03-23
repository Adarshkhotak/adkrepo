class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


"""
Time complexity -> O(N/2)
N is the number of nodes

Space complexity -> O(1)
"""


def findPairs(head: Node, k: int) :
    result = []
    left = head
    right = head
    while right.next:
        right = right.next
    while left and right and left.data < right.data:
        total = left.data + right.data    #this total method for cond is good then by value
        if total == k:
            result.append([left.data, right.data])
            right = right.prev
            left = left.next
        elif total > k:
            right = right.prev
        else:
            left = left.next
    return result