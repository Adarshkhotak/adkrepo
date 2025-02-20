# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def oddEvenList(self, head:ListNode) -> ListNode:
        if head is None:
            return head
        odd=head
        even=head.next
        even_head=even
        while even and even.next:
            odd.next=even.next   #to connect odd to odd
            odd=odd.next  #moving odd
            even.next=odd.next    #to connect even to even
            even=even.next
        
        odd.next=even_head  #connecting odd and even

        return head
        

        