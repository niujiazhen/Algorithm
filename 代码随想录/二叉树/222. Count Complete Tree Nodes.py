# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #前序遍历记录节点个数
        # return self.traversal(root)
        #完全二叉树算法
        return self.fullBinaryTreeTraversal(root)


    # 前序遍历记录节点个数（适应所有二叉树）
    def traversal(self,cur:TreeNode)->int:
        if not cur:
            return 0
        leftNum = self.traversal(cur.left)  # 左
        rightNum = self.traversal(cur.right)  # 右
        treeNum = leftNum + rightNum + 1  # 中
        return treeNum

    #完全二叉树算法，只记录左右最外侧深度即可判定完全二叉树是不是满二叉树，若是满二叉树则直接用节点计算公式即可，相当于剪支了中间的节点遍历
    def fullBinaryTreeTraversal(self,cur:TreeNode)->int:
        if not cur:
            return 0
        leftDepth=1#记录左子树深度
        rightDepth=1#记录右子树深度
        left=cur.left
        right=cur.right
        while left:
            leftDepth+=1
            left=left.left#由于是完全二叉树，只记录最左侧的深度
        while right:
            rightDepth+=1
            right=right.right#由于是完全二叉树，只记录最右侧的深度
        if leftDepth==rightDepth:#如果完全二叉树的左右深度相等，则为满二叉树
            return pow(2,leftDepth)-1#满二叉树节点快速计算公式
        return self.fullBinaryTreeTraversal(cur.left)+self.fullBinaryTreeTraversal(cur.right)+1#当前节点的子数不是满二叉树，则记录当前节点，继续递归左右子树是否为满二叉树






if __name__ == '__main__':
    solution=Solution()
    treeNode1 = TreeNode(1)
    treeNode2 = TreeNode(2)
    treeNode3 = TreeNode(2)
    treeNode4 = TreeNode(3)
    treeNode5 = TreeNode(4)
    treeNode6 = TreeNode(4)

    treeNode1.left=treeNode2
    treeNode1.right=treeNode3
    treeNode2.left=treeNode4
    treeNode2.right=treeNode5
    treeNode3.left=treeNode6

    print(solution.countNodes(treeNode1))
