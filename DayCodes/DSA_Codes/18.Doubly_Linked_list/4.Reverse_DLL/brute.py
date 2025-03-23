def reverseDLL(head):
    temp=head
    stack=[]
    while temp:
        stack.append(temp.data)
        temp=temp.next
    temp=head
    while temp:
        temp.data=stack.pop()
        temp=temp.next
    return head