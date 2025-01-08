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
            level_stack=[]#用于记录当前层的所有节点,stack反转了所有节点值
            for i in range(size):#这一次循环拿出所有下一层节点，并记录值
                node=queue[i]#拿到当前要处理的节点
                if node.left:
                    level_stack.append(node.left.val)#记录当前节点左节点
                    queue.append(node.left)#记录下一层要处理的节点
                if node.right:
                    level_stack.append(node.right.val)  # 记录当前节点右节点
                    queue.append(node.right)#记录下一层要处理的节点
            for i in range(size):#这一层遍历用于反转节点值
                node=queue.popleft()
                if node.left:
                    node.left.val=level_stack.pop()#反转节点值
                if node.right:
                    node.right.val=level_stack.pop()#反转节点值
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

    print(solution.invertTree(treeNode1))
