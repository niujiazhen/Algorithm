# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #T=O(n), S=O(N/2) in worst case
        queue=deque()
        queue.append(root)
        size=1#record the number of nodes to handle in current level
        ans=[]
        while queue:
            sum=0
            num=0
            for i in range(size):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                sum+=node.val
                num+=1
            ans.append(sum/num)
            size=len(queue)
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
    print(solution.averageOfLevels(treeNode1))