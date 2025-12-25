# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #We use Divide and Conquer
        #T=O(n) S=O(logn)
        def buildBST(l:int,r:int)->TreeNode:
            if l>r:
                return None
            #we always choose the right middle num as the current node
            mid=(l+r)//2
            node=TreeNode(nums[mid])
            node.left=buildBST(l,mid-1)
            node.right=buildBST(mid+1,r)
            return node
        return buildBST(0,len(nums)-1)




if __name__ == '__main__':
    solution=Solution()
    print(solution.sortedArrayToBST([-10,-3,0,5,9]))