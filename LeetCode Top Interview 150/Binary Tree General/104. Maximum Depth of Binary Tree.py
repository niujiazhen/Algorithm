# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:#means the parent of current node is the leaf node
            return 0
        #Recursively calculate the depth of the left and right node
        left_height=self.maxDepth(root.left)
        right_height=self.maxDepth(root.right)

        #the depth of the node is the max of left and right child node, and plus 1(the node itself)
        return max(left_height,right_height)+1




if __name__ == '__main__':
    solution=Solution()
    treeNode1 = TreeNode(3)
    treeNode2 = TreeNode(9)
    treeNode3 = TreeNode(20)
    treeNode4 = TreeNode(15)
    treeNode5 = TreeNode(7)
    treeNode1.left=treeNode2
    treeNode1.right=treeNode3
    treeNode3.left=treeNode4
    treeNode3.right=treeNode5
    print(solution.maxDepth(treeNode1))
