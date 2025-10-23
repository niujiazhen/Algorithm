# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = None#record the ans

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.recurse_tree(root,p,q)
        return self.ans

    def recurse_tree(self,node:TreeNode,p:TreeNode,q:TreeNode)->bool:
        #T=O(n), S=O(n)
        #Edge Case
        if not node:
            return False
        #find p or q in left subtree
        left=self.recurse_tree(node.left,p,q)

        #find p or q in right subtree
        right=self.recurse_tree(node.right,p,q)

        #check if the current node is p or q
        mid=0
        if node==p or node==q:
            mid=1

        if mid+left+right>=2:#the current node is the LCA of p and q
            self.ans=node

        return mid or left or right#either the left subtree or the right subtree or the current node is p or q is valid





if __name__ == '__main__':
    solution=Solution()
    node1=TreeNode(3)
    node2=TreeNode(5)
    node3=TreeNode(1)
    node4=TreeNode(6)
    node5=TreeNode(2)
    node6=TreeNode(0)
    node7=TreeNode(8)
    node8=TreeNode(7)
    node9=TreeNode(4)

    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.right=node5
    node3.left=node6
    node3.right=node7
    node5.left=node8
    node5.right=node9
    print(solution.lowestCommonAncestor(node1,node2,node3))