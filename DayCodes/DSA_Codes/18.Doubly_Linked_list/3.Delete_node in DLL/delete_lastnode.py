def deleteLastNode(head) :
    if head is None or head.next is None:
        return None
    current=head
    previos=None
    while current.next is not None:
        previos=current
        current=current.next
    previos.next=None
        

    return head

#OR
def deleteLastNode(head):
    if head is None or head.next is None:
        return None
    temp=head
    while temp.next.next is not None:
        temp=temp.next
        
    #temp.next=None  he use kel tr khal che 2 lines kad
    temp.next.prev=None
    temp.next=None

    return head