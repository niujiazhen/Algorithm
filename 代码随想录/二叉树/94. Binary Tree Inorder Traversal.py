# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        # self.recursiveTraversal(ans,root)
        self.iterativeTraversal(ans,root)
        return ans


    def recursiveTraversal(self, ans:List, cur:TreeNode)->None:#递归法中序遍历
        if(not cur):
            return
        self.recursiveTraversal(ans,cur.left)
        ans.append(cur.val)
        self.recursiveTraversal(ans,cur.right)

    def iterativeTraversal(self, ans:List, root:TreeNode)->None:#迭代法中序遍历
        if not root:
            return
        cur=root#cur记录当前处理的节点
        stack=[]#stack保存访问过的节点
        while cur or stack:
            if cur:#先迭代访问到最底层的左节点，并保存
                stack.append(cur)
                cur=cur.left
            else:#开始处理当前节点
                cur=stack.pop()#取出当前要处理的节点，这一步即处理左节点也处理中节点
                ans.append(cur.val)#存入当前节点
                cur=cur.right#处理栈顶元素右节点
        return









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
    print(solution.inorderTraversal(treeNode1))
