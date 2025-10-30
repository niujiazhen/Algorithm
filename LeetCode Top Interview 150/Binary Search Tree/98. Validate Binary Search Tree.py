# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #T=O(n), S=O(n)
        inorderList=[]
        self.inorderTraverse(root,inorderList)
        for i in range(len(inorderList)-1):
            if inorderList[i+1]<=inorderList[i]:
                return False
        return True

    def inorderTraverse(self,node:TreeNode,num:List[int]):
        if not node:
            return
        self.inorderTraverse(node.left,num)
        num.append(node.val)
        self.inorderTraverse(node.right,num)




if __name__ == '__main__':
    solution=Solution()
    print(solution.isValidBST())
