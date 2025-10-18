# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Divide and Conquer:
        #the preorder keeps track of the element to construct the tree
        def array_to_tree(left:int, right:int):
            nonlocal preorder_index
            if left>right:#
                return None
            #select the preorder_index element as a root and increment it
            root=TreeNode()
            root.val=preorder[preorder_index]
            root_val=root.val
            preorder_index+=1

            #build left and right subtrees
            root.left=array_to_tree(left,inorder_index_map[root_val]-1)
            root.right=array_to_tree(inorder_index_map[root_val]+1,right)

            return root


        preorder_index=0
        #build a hashmap to store value->index of inorder tree
        inorder_index_map={}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)


if __name__ == '__main__':
    solution=Solution()

    print(solution.buildTree([3,9,20,15,7],[9,3,15,20,7]))