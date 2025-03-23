#GFG solu imp chk
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

def addNode(head, p, data):
    new_node=Node(data)
    temp=head
    count=0
    while temp.next:
        if count==p:  #it is insert after
            break
        count+=1
        temp=temp.next
    new_node.next=temp.next
    new_node.prev=temp
    temp.next=new_node
        
    return head