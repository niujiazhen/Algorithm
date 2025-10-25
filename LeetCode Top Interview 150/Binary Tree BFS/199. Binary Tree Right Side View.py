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
        #We use level order traverse to see the right side element of each level
        #T=O(n), S=O(N/2) in worst case
        if not root:
            return []
        queue=deque()
        queue.append(root)
        size=1#record the number of nodes to handle in current level
        ans=[]
        while queue:
            for i in range(size):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == size-1:
                    ans.append(node.val)
            size=len(queue)
        return ans


if __name__ == '__main__':
    solution=Solution()
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(5)

    node1.left=node2
    node1.right=node3
    node2.right=node5
    node3.right=node4
    print(solution.rightSideView(node1))