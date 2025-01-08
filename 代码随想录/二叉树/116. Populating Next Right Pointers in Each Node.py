# Definition for a Node.
from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue=deque()
        queue.append(root)
        size=1
        while queue:
            pre=None#记录上一个节点
            for i in range(size):
                node=queue.popleft()
                if pre:
                    pre.next=node#记录next节点
                pre=node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            size=len(queue)#获取下一层要处理的节点数量
        return root


if __name__ == '__main__':
    solution=Solution()
