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
        def array_to_tree(left:int, right:int):
            nonlocal preorder_index
            if left > right:
                return None
            root_val = postorder.pop()  # the root val
            root = TreeNode(root_val)  # the current root node

            # then we build the left and right subtrees
            # find the D&C boundries in inorder tree
            #build left and right subtrees
            root.right=array_to_tree(inorder_index_map[root_val]+1,right)
            root.left = array_to_tree(left, inorder_index_map[root_val] - 1)
            return root


        preorder_index=0
        #build a hashmap to store value->index of inorder tree
        inorder_index_map={}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(inorder) - 1)



if __name__ == '__main__':
    solution=Solution()
    print(solution.buildTree([9,3,15,20,7],[9,15,7,20,3]))