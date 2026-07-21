# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #T=O(n）, S=O(n)
        #we do two traverse to check if the two tree is same
        # ans1=[]
        # ans2=[]
        # self.preOrderTraverse(ans1,p)
        # self.preOrderTraverse(ans2,q)
        # return ans1==ans2

        if not p and not q:#both parent nodes have no child node, same
            return True
        elif not p or not q:#one of the parent node has child node, not same
            return False
        elif p.val!=q.val:#not same in value
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

    def preOrderTraverse(self,ans:list,root:TreeNode):
        if not root:
            ans.append(None)#is important because two different tree could have same traverse order
            return
        ans.append(root.val)
        self.preOrderTraverse(ans,root.left)
        self.preOrderTraverse(ans,root.right)



if __name__ == '__main__':
    solution=Solution()
    ptreeNode1=TreeNode(1)
    ptreeNode2=TreeNode(2)
    ptreeNode3=TreeNode(3)

    ptreeNode1.left=ptreeNode2
    ptreeNode1.right=ptreeNode3

    qtreeNode1=TreeNode(1)
    qtreeNode2=TreeNode(2)
    qtreeNode3=TreeNode(3)

    qtreeNode1.left=qtreeNode2
    qtreeNode1.right=qtreeNode3

    print(solution.isSameTree(ptreeNode1,qtreeNode1))
