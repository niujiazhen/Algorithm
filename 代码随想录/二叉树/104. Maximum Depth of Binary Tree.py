# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxDepth=0#记录最大深度
        queue=collections.deque()
        queue.append(root)
        size=1#记录当前层数要处理的节点数量
        while queue:#采用层序遍历来记录最大深度
            maxDepth+=1
            for i in range(size):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            size=len(queue)#记录下一层要处理的节点数量
        return maxDepth




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
    print(solution.maxDepth(treeNode1))

