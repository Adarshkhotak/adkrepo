class Solution:
    def reverseDLL(self, head):
        temp=head
        pri=None
        while temp:
            front=temp.next
            temp.next=pri
            pri=temp
            temp=front
        return pri