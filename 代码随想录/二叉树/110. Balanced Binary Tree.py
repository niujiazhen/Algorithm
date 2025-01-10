# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.get_height(root)==-1:
            return False
        return True



    def get_height(self,cur:TreeNode)->int:#返回当前节点的高度，高度采用后序遍历，左右中
        if not cur:#如果是空节点则高度为0（即上一层为叶子节点，高度为1）
            return 0
        left_height=self.get_height(cur.left)#获取左子树的高度
        right_height=self.get_height(cur.right)#获取右子树的高度
        if left_height==-1:#如果当前节点的左子树已经不是平衡二叉树了，那么向上的节点也一定不是平衡二叉树*
            return -1
        elif right_height==-1:#如果当前节点的右子树已经不是平衡二叉树了，那么向上的节点也一定不是平衡二叉树*
            return -1
        else:#左子树和右子树都是平衡二叉树的情况下
            if abs(left_height-right_height)>1:#当前左右子树高度差超过1，则当前节点不是平衡二叉树
                return -1
            else:#当前节点是平衡二叉树，则计算高度
                height=1+max(left_height,right_height)#当前节点高度=左右子树最大高度+当前节点高度1
                return height




if __name__ == '__main__':
    solution = Solution()
    treeNode1 = TreeNode(3)
    treeNode2 = TreeNode(9)
    treeNode3 = TreeNode(20)
    treeNode4 = TreeNode(15)
    treeNode5 = TreeNode(7)
    treeNode1.left = treeNode2
    treeNode1.right = treeNode3
    treeNode3.left = treeNode4
    treeNode3.right = treeNode5

    print(solution.isBalanced(treeNode1))
