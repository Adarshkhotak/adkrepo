from typing import List
from collections import deque


def levelOrder(root) -> List[int]:
    queue=deque()
    queue.append(root)
    res=[]
    while len(queue)!=0:
        node=queue.popleft()  #IMP popleft
        res.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res