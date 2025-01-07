# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        result=[]
        queue=deque()
        queue.append(root)
        size=1
        while queue:
            sum=0
            num=size
            while size:
                node=queue.popleft()
                sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size-=1
            size=len(queue)
            result.append(sum/num)
        return result





if __name__ == '__main__':
    solution = Solution()
    treeNode1 = TreeNode(3)
    treeNode2 = TreeNode(9)
    treeNode3 = TreeNode(20)
    treeNode4 = TreeNode(15)
    treeNode5 = TreeNode(7)
    treeNode1.left = treeNode2
    treeNode1.right = treeNode3
    treeNode3.left = treeNode4
    treeNode3.right = treeNode5
    print(solution.averageOfLevels(treeNode1))
