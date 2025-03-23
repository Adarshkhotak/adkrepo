
class Node:
    def __init__(self, val=None) -> None:
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        # if self.head is None:
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        if not self.head:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def insert_at(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
           
            count = 0
            while current:
                count+=1
                #current=current.next
                if count==position:
                    break
                current=current.next   
            new_node.next = current.next
            # if prev_node is not None:
            current.next = new_node

    def delete_head(self):
        if not self.head:
            print("Cannot delete, SLL is already empty")
        else:
            self.head = self.head.next

    def delete(self, data):
        temp = self.head
        if temp.next is not None:
            if temp.val == data:
                self.head = temp.next
                return
            else:
                found = False
                while temp is not None:
                    if temp.val == data:
                        found = True
                        break
                    prev = temp
                    temp = temp.next

                if found:
                    prev.next = temp.next
                    return
                else:
                    print("Node not found")


sll = SinglyLinkedList()
sll.append(100)
sll.append(200)
sll.append(50)
sll.append(20)
sll.insert_at(43, 1)
sll.insert_at(400, 3)
sll.traverse()

