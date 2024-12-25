# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        self.traversal(ans,root)
        return ans


    def traversal(self, ans:List, cur:TreeNode)->None:#递归法前序遍历
        if(not cur):
            return
        ans.append(cur.val)
        self.traversal(ans,cur.left)
        self.traversal(ans,cur.right)






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
    print(solution.postorderTraversal(treeNode1))
