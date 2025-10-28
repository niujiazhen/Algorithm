# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:







if __name__ == '__main__':
    solution=Solution()
    node1=TreeNode(4)
    node2=TreeNode(2)
    node3=TreeNode(6)
    node4=TreeNode(1)
    node5=TreeNode(3)

    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.right=node5
    print(solution.getMinimumDifference(node1))