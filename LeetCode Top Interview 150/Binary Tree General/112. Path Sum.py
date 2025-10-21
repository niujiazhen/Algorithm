# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.preOrderTraverse(root,0,targetSum)

    def preOrderTraverse(self,node:TreeNode,sum:int,targetSum:int)->bool:
        if not node:
            return False
        sum+=node.val
        if not node.left and not node.right:#we reach the leaf node
            if sum==targetSum:
                return True
        return self.preOrderTraverse(node.left,sum,targetSum) or self.preOrderTraverse(node.right,sum,targetSum)




if __name__ == '__main__':
    solution=Solution()
    node1=TreeNode(5)
    node2=TreeNode(4)
    node3=TreeNode(8)
    node4=TreeNode(11)
    node5=TreeNode(13)
    node6=TreeNode(4)
    node7=TreeNode(7)
    node8=TreeNode(2)
    node9=TreeNode(1)

    node1.left=node2
    node1.right=node3
    node2.left=node4
    node3.left=node5
    node3.right=node6
    node4.left=node7
    node4.right=node8
    node6.right=node9
    print(solution.hasPathSum(node1,22))