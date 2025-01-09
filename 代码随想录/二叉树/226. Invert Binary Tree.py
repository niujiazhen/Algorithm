# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue=collections.deque()
        queue.append(root)
        while queue:
            size=len(queue)#当前层需要处理的节点
            for i in range(size):#这一次循环拿出所有下一层节点
                node=queue.popleft()#拿到当前要处理的节点
                node.left,node.right=node.right,node.left#交换节点
                if node.left:
                    queue.append(node.left)#将下一层要处理的节点放入queue
                if node.right:
                    queue.append(node.right)#将下一层要处理的节点放入queue

        return root



if __name__ == '__main__':
    solution = Solution()
    treeNode1 = TreeNode(4)
    treeNode2 = TreeNode(2)
    treeNode3 = TreeNode(7)
    treeNode4 = TreeNode(1)
    treeNode5 = TreeNode(3)
    treeNode6 = TreeNode(6)
    treeNode7 = TreeNode(9)

    treeNode1.left = treeNode2
    treeNode1.right = treeNode3
    treeNode2.left = treeNode4
    treeNode2.right = treeNode5
    treeNode3.left = treeNode6
    treeNode3.right = treeNode7
    #
    # treeNode1 = TreeNode(1)
    # treeNode2 = TreeNode(2)
    # treeNode1.left=treeNode2

    print(solution.invertTree(treeNode1))
