# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.recursiveTraversal(ans,root)#递归法前序遍历
        self.iterativeTraversal()#迭代法前序遍历
        return ans


    def recursiveTraversal(self, ans:List, cur:TreeNode)->None:#递归法前序遍历
        if(not cur):
            return
        ans.append(cur.val)
        self.recursiveTraversal(ans,cur.left)
        self.recursiveTraversal(ans,cur.right)

    def iterativeTraversal(self, ans:List, cur:TreeNode)->None:#迭代法前序遍历








if __name__ == '__main__':
    solution=Solution()
    treeNode1=TreeNode(1)
    treeNode2=TreeNode(2)
    treeNode3=TreeNode(3)
    treeNode4=TreeNode(4)
    treeNode5=TreeNode(5)
    treeNode6=TreeNode(6)
    treeNode7=TreeNode(7)
    treeNode8=TreeNode(8)
    treeNode9=TreeNode(9)

    treeNode1.left=treeNode2
    treeNode1.right=treeNode3
    treeNode2.left=treeNode4
    treeNode2.right=treeNode5
    treeNode5.left=treeNode6
    treeNode5.right=treeNode7
    treeNode3.right=treeNode8
    treeNode8.left=treeNode9
    print(solution.preorderTraversal(treeNode1))
