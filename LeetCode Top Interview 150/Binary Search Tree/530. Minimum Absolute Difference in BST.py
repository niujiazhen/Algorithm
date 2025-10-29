# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #we can get a sorted array if we do inorder traverse due to the property of Binary Search Tree
        inorderList=[]
        self.inOrderTraverse(root,inorderList)
        minDiff=float('inf')
        for i in range(len(inorderList)-1):
            minDiff=min(minDiff,inorderList[i+1]-inorderList[i])
        return minDiff

    def inOrderTraverse(self,node:TreeNode,num:List[int]):
        if not node:
            return
        self.inOrderTraverse(node.left,num)
        num.append(node.val)
        self.inOrderTraverse(node.right,num)




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