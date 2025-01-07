# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]#保存答案
        queue = deque()
        queue.append(root)  # 从根节点开始遍历
        size = 1  # 用于记录当前层有多少节点需要弹出
        while queue and size:
            ans = []  # 记录当前层的节点
            #先把当前层的节点都弹出
            while size:
                node=queue.popleft()#记录弹出的节点
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                ans.append(node.val)
                size-=1
            size+=len(queue)
            result.append(ans)
        return result









if __name__ == '__main__':
    solution=Solution()
    treeNode1 = TreeNode(3)
    treeNode2 = TreeNode(9)
    treeNode3 = TreeNode(20)
    treeNode4 = TreeNode(15)
    treeNode5 = TreeNode(7)
    treeNode1.left=treeNode2
    treeNode1.right=treeNode3
    treeNode3.left=treeNode4
    treeNode3.right=treeNode5
    print(solution.levelOrder(treeNode1))