# Definition for a binary tree node.
import collections
from socket import send_fds
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left,root.right)

    def compare(self,left:TreeNode,right:TreeNode)->bool:
        if not left and not right:#如果左右节点都不存在，说明当前节点是叶子节点，符合对称
            return True
        elif not left:#只有左节点不存在，不对称
            return False
        elif not right:#只有右节点不存在，不对称
            return False
        elif left.val!=right.val:#左右节点都存在，但值不同，不对称
            return False
        #接下来处理左右节点都存在，且值相同，这种情况是对称的
        outside=self.compare(left.left,right.right)#比较外侧节点值是否相同
        inside=self.compare(left.right,right.left)#比较内侧节点值是否相同
        return outside and inside






if __name__ == '__main__':
    solution=Solution()
    treeNode1 = TreeNode(1)
    treeNode2 = TreeNode(2)
    treeNode3 = TreeNode(2)
    treeNode4 = TreeNode(3)
    treeNode5 = TreeNode(4)
    treeNode6 = TreeNode(4)
    treeNode7 = TreeNode(3)

    treeNode1.left=treeNode2
    treeNode1.right=treeNode3
    treeNode2.left=treeNode4
    treeNode2.right=treeNode5
    treeNode3.left=treeNode6
    treeNode3.right=treeNode7

    print(solution.isSymmetric(treeNode1))

