# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        #Use iterative Traverse to flat the tree
        #T=O(n), S=O(n)
        if not root:
            return None
        stack=[]
        stack.append(root)
        preOrder=[]
        while stack:
            node=stack.pop()
            if node.right:#due to FILO, we should first push the right node into the stack, then we will first handle the left node
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            preOrder.append(node)
        for i in range(len(preOrder)-1):
            preOrder[i].left=None
            preOrder[i].right=preOrder[i+1]
        return root

        # Use recursive Traverse to flat the tree
        # T=O(n), S=O(n)
        preOrder = []
        self.preOrderTraverse(root, preOrder)
        for i in range(len(preOrder) - 1):
            preOrder[i].left = None
            preOrder[i].right = preOrder[i + 1]

    def preOrderTraverse(self, root: TreeNode, preOrder: List[TreeNode]) -> None:
        if not root:
            return None
        preOrder.append(root)
        self.preOrderTraverse(root.left, preOrder)
        self.preOrderTraverse(root.right, preOrder)



if __name__ == '__main__':
    solution=Solution()
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(5)
    node4=TreeNode(3)
    node5=TreeNode(4)
    node6=TreeNode(6)

    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.right=node5
    node3.right=node6
    print(solution.flatten(node1))
