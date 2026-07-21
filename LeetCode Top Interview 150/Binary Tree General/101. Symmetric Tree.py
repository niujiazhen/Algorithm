# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #recursive method T=O(n), S=O(n)
        return self.isMirror(root,root)

    def isMirror(self,node1:TreeNode, node2:TreeNode)->bool:
        if not node1 and not node2:#current node is a leaf node
            return True
        elif not node1 or not node2:#not symmetric
            return False
        return (node1.val==node2.val) and self.isMirror(node1.left,node2.right) and self.isMirror(node1.right,node2.left)#recursively traverse





if __name__ == '__main__':
    solution=Solution()
    treeNode1 = TreeNode(1)
    treeNode2 = TreeNode(2)
    treeNode3 = TreeNode(2)
    treeNode4 = TreeNode(3)
    treeNode5 = TreeNode(4)
    treeNode6 = TreeNode(4)
    treeNode7 = TreeNode(3)

    treeNode1.left = treeNode2
    treeNode1.right = treeNode3
    treeNode2.left = treeNode4
    treeNode2.right = treeNode5
    treeNode3.left = treeNode6
    treeNode3.right = treeNode7
    print(solution.isSymmetric(treeNode1))
