# Definition for a binary tree node.
from inspect import stack
from time import sleep
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #we use the property of Binary Search Tree
        #T=O(n), S=O(n)
        # inorderList=[]
        # self.inorderTraverse(root,inorderList)
        # return inorderList[k-1]

        #Method2: we only have to traverse the first k th element
        #T=O(k), S=O(k)
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left#keep pushing the smaller element into stack
            root=stack.pop()#pop the currently smallest element
            k-=1
            if not k:#means the current roor is the kth smallest element
                return root.val
            root=root.right#keep pushing element that is bigger than left and mid




    def inorderTraverse(self, node:TreeNode, num:List[int]):
        if not node:
            return
        self.inorderTraverse(node.left,num)
        num.append(node.val)
        self.inorderTraverse(node.right,num)



if __name__ == '__main__':
    solution=Solution()
    node1=TreeNode(3)
    node2=TreeNode(1)
    node3=TreeNode(4)
    node4=TreeNode(2)

    node1.left=node2
    node1.right=node3
    node2.right=node4
    print(solution.kthSmallest(node1,1))
