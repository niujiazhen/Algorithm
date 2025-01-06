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
        # self.recursiveTraversal(ans,root)#递归法后序遍历
        # return ans
        return self.iterativeTraversal(ans,root)#迭代法后序遍历


    def recursiveTraversal(self, ans:List, cur:TreeNode)->None:#递归法后序遍历
        if(not cur):
            return
        self.recursiveTraversal(ans,cur.left)
        self.recursiveTraversal(ans,cur.right)
        ans.append(cur.val)

    def iterativeTraversal(self, ans:List, root:TreeNode)->List[int]:#迭代法后序遍历
        if(not root):
            return []
        stack=[root]
        while(stack):#前序遍历迭代法处理顺序为中右左，后序遍历可以先将前序遍历转为中左右，再反转ans变为左右中即可
            node=stack.pop()
            ans.append(node.val)
            if(node.left):
                stack.append(node.left)
            if(node.right):
                stack.append(node.right)
        return ans[::-1]








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
