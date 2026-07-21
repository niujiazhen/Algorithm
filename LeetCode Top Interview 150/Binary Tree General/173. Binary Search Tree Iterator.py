# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        #T=O(n), S=O(n)
        self.preOrderList=[]
        self.preOrderIndex=0
        self.preOrderTraversal(root,self.preOrderList)
    def preOrderTraversal(self,node:TreeNode,ans:List[int]):
        if not node:
            return
        self.preOrderTraversal(node.left,ans)
        ans.append(node.val)
        self.preOrderTraversal(node.right,ans)


    def next(self) -> int:
        #T=O(1)
        val=self.preOrderList[self.preOrderIndex]
        self.preOrderIndex+=1
        return val

    def hasNext(self) -> bool:
        # T=O(1)
        return self.preOrderIndex<len(self.preOrderList)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == '__main__':
    node1=TreeNode(7)
    node2=TreeNode(3)
    node3=TreeNode(15)
    node4=TreeNode(9)
    node5=TreeNode(20)
    node1.left=node2
    node1.right=node3
    node3.left=node4
    node3.right=node5
    bst=BSTIterator(node1)
