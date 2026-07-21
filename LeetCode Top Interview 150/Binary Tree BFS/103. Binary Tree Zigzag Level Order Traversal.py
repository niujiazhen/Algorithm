# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #T=O(n), S=O(1)
        # T=O(n), S=O(N/2) in worst case
        if not root:
            return []
        queue = deque()
        queue.append(root)
        size = 1  # record the number of nodes to handle in current level
        ans = []
        flag=1#record whether to reverse the list
        while queue:
            res=[]
            for i in range(size):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                res.append(node.val)
            size=len(queue)
            if flag==1:
                ans.append(res)
            else:
                ans.append(res[::-1])
            flag=-flag
        return ans



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
    print(solution.zigzagLevelOrder(treeNode1))