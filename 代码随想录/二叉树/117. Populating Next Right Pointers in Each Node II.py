"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue=deque()
        queue.append(root)
        size=1
        while queue:
            pre=None
            for i in range(size):
                node=queue.popleft()
                if pre:
                    pre.next=node
                pre=node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            size=len(queue)
        return root
        
