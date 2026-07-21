# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Global variable to track the maximum path sum
        self.max_sum = float('-inf')

        def gain_from_subtree(node: TreeNode) -> int:
            # Base case: null node contributes 0 to path sum
            if not node:
                return 0

            # Recursively compute the maximum gain from left and right subtrees
            left_gain = max(gain_from_subtree(node.left), 0)
            right_gain = max(gain_from_subtree(node.right), 0)

            # Path sum that passes through the current node
            # (can include both left and right children)
            current_path_sum = node.val + left_gain + right_gain

            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the maximum gain that can be extended to the parent
            # (only one side can be chosen to avoid path branching)
            return node.val + max(left_gain, right_gain)

        # Start DFS from the root
        gain_from_subtree(root)

        return self.max_sum

if __name__ == '__main__':
    solution=Solution()
    treeNode1 = TreeNode(-10)
    treeNode2 = TreeNode(9)
    treeNode3 = TreeNode(20)
    treeNode4 = TreeNode(15)
    treeNode5 = TreeNode(7)
    treeNode1.left=treeNode2
    treeNode1.right=treeNode3
    treeNode3.left=treeNode4
    treeNode3.right=treeNode5
    print(solution.maxPathSum(treeNode1))