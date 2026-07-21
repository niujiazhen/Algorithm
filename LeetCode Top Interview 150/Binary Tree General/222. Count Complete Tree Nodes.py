# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #T=O(n), S=O(n)
        # nodeList=[]
        # self.preOrderTraverse(root,nodeList)
        # return len(nodeList)

        #T=O(n), S=O(logn)
        if not root:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

    def preOrderTraverse(self, node:TreeNode, nodeList:List[int]):
        if not node:
            return
        nodeList.append(node.val)
        self.preOrderTraverse(node.left, nodeList)
        self.preOrderTraverse(node.right, nodeList)





if __name__ == '__main__':
    solution=Solution()
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(5)
    node6=TreeNode(6)

    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.right=node5
    node3.left=node6
    print(solution.countNodes(node1))