# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]
        queue=deque()
        queue.append(root)
        size=1
        while queue:
            maxNode=float('-inf')#记录每一层最大值
            while size:
                node=queue.popleft()
                maxNode=max(maxNode,node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size-=1
            size=len(queue)
            result.append(maxNode)
        return result




if __name__ == '__main__':
    solution=Solution()
    treeNode1 = TreeNode(1)
    treeNode2 = TreeNode(3)
    treeNode3 = TreeNode(2)
    treeNode4 = TreeNode(5)
    treeNode5 = TreeNode(3)
    treeNode6 = TreeNode(9)

    treeNode1.left=treeNode2
    treeNode1.right=treeNode3
    treeNode2.left=treeNode4
    treeNode2.right=treeNode5
    treeNode3.right=treeNode6

    print(solution.largestValues(treeNode1))
