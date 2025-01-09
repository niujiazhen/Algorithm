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






    def traversal(self,cur:TreeNode)->int:#前序遍历记录节点个数（适应所有二叉树）
        if not cur:
            return 0
        leftNum = self.traversal(cur.left)  # 左
        rightNum = self.traversal(cur.right)  # 右
        treeNum = leftNum + rightNum + 1  # 中
        return treeNum




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
