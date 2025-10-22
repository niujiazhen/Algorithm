# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #T=O(n), S=O(1)
        return self.preOrderTraverse(root,0)


    def preOrderTraverse(self,node:TreeNode, sum:int)->int:
        if not node:
            return 0
        sum=sum*10+node.val
        if not node.left and not node.right:#means the current node is a leaf node
            return sum
        return self.preOrderTraverse(node.left,sum)+self.preOrderTraverse(node.right,sum)
    #the difference of passing parameters like int or str is that,






if __name__ == '__main__':
    solution=Solution()
    node1=TreeNode(4)
    node2=TreeNode(9)
    node3=TreeNode(0)
    node4=TreeNode(5)
    node5=TreeNode(1)

    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.right=node5
    print(solution.sumNumbers(node1))