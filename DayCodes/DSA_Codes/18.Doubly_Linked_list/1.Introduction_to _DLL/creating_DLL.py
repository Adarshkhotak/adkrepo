
# Node Class
class Node:
	def __init__(self, data):# data -> value stored in node
	    self.data = data
	    #self.next = None  ugach # kelay ha
	    #self.prev = None

class Solution:
    def constructDLL(self, arr):
        new_head=Node(arr[0])
        current_node=new_head
        for i in range(1,len(arr)):
            new_node=Node(arr[i])
            current_node.next=new_node
            new_node.prev=current_node
            current_node=new_node
        return new_head