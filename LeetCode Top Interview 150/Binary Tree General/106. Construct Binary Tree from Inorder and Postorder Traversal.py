# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #Divide and Conquer: T=O(n), S=O(n)
        #the postorder keeps track of the element to construct the tree
        inOrderMap={}
        for i in range(len(inorder)):
            inOrderMap[inorder[i]]=i

        def buildSubTree(left:int, right:int)->TreeNode:
            if left>right:
                return None
            # the root node is at the end of postOrder
            nodeValue=postorder.pop()
            node=TreeNode(nodeValue)

            # We create the right subtree first because of postOrder
            node.right=buildSubTree(inOrderMap[nodeValue]+1,right)
            node.left=buildSubTree(left,inOrderMap[nodeValue]-1)

            return node

        return buildSubTree(0,len(inorder)-1)


if __name__ == '__main__':
    solution=Solution()
    print(solution.buildTree([9,3,15,20,7],[9,15,7,20,3]))