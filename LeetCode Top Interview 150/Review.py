# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # We use Divide and Conquer
        def buildTree(left:int,right:int)->TreeNode:
            if left>right:
                return None
            p=(left+right)//2# we divide the problem at the middle left point
            treeNode=TreeNode(nums[p])
            #Divide and Conquer
            treeNode.left=buildTree(left,p-1)
            treeNode.right=buildTree(p+1,right)

            return treeNode


        return buildTree(0,len(nums)-1)


if __name__ == '__main__':
    solution=Solution()
    print(solution.sortedArrayToBST([-10,-3,0,5,9]))