'''TC=O(2N),SC=O(1)'''
class Solution:
    def deleteMiddle(self, head):
        temp=head
        n=0
        while temp:
            n+=1
            temp=temp.next
        if head.next is None: #edge case [1]
            return None    
        temp=head
        for i in range(n//2-1):
            temp=temp.next
        temp.next=temp.next.next
        return head