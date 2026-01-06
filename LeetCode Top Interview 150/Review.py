# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Divide and Conquer: T=O(n), S=O(n)
        #the preorder keeps track of the element to construct the tree
        inOrderMap={}# records the value->key map for inorderList
        for i in range(len(inorder)):
            inOrderMap[inorder[i]]=i

        def buildSubTree(left:int, right:int)->TreeNode:
            nonlocal preOrderIndex
            if left>right:
                return None
            # Create the node
            nodeValue=preorder[preOrderIndex]
            node=TreeNode(nodeValue)
            preOrderIndex+=1

            # Recursively create the subtrees
            node.left=buildSubTree(left,inOrderMap[nodeValue]-1)
            node.right=buildSubTree(inOrderMap[nodeValue]+1,right)

            return node

        return buildSubTree(0,len(preorder)-1)



if __name__ == '__main__':
    solution=Solution()

    print(solution.buildTree([3,9,20,15,7],[9,3,15,20,7]))