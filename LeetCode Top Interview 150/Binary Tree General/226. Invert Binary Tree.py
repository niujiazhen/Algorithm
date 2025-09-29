# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #T=O(n)
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right=root.right,root.left
        return root




if __name__ == '__main__':
    solution=Solution()
    treeNode1 = TreeNode(4)
    treeNode2 = TreeNode(2)
    treeNode3 = TreeNode(7)
    treeNode4 = TreeNode(1)
    treeNode5 = TreeNode(3)
    treeNode6 = TreeNode(6)
    treeNode7 = TreeNode(9)

    treeNode1.left = treeNode2
    treeNode1.right = treeNode3
    treeNode2.left = treeNode4
    treeNode2.right = treeNode5
    treeNode3.left = treeNode6
    treeNode3.right = treeNode7
    print(solution.invertTree(treeNode1))
