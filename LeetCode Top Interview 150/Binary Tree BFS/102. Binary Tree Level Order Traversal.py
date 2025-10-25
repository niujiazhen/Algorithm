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
        #T=O(n), S=O(1)
        # T=O(n), S=O(N/2) in worst case
        if not root:
            return []
        queue = deque()
        queue.append(root)
        size = 1  # record the number of nodes to handle in current level
        ans = []
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
            ans.append(res)
        return ans





if __name__ == '__main__':
    solution=Solution()
    print(solution.levelOrder())