from collections import deque
from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue=deque()
        queue.append(root)
        size=1
        while queue:
            ans=[]
            while size:
                node=queue.popleft()
                ans.append(node.val)
                if node.children:
                    for i in range(len(node.children)):
                        queue.append(node.children[i])
                size-=1
            size=len(queue)
            result.append(ans)
        return result