# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result=[]#记录答案
        queue=deque()#层序遍历记录每一层
        queue.append(root)
        size=1
        while queue:
            ans=[]#记录每一层要弹出的节点
            while size:
                node=queue.popleft()
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size-=1
            size=len(queue)
            result.append(ans[-1])#result只记录每一层最右侧节点
        return result





if __name__ == '__main__':
    solution=Solution()
    treeNode1 = TreeNode(1)
    treeNode2 = TreeNode(2)
    treeNode3 = TreeNode(3)
    treeNode4 = TreeNode(4)
    treeNode5 = TreeNode(5)
    treeNode1.left = treeNode2
    treeNode1.right = treeNode3
    treeNode2.right=treeNode5
    treeNode3.right=treeNode4
    print(solution.rightSideView(treeNode1))
