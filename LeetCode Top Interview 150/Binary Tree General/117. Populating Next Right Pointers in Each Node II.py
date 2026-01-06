from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: Node) -> Node:
        # we use the level order to connect each node's next pointer to its next right node
        # T=O(n), S=O(n)
        # Edge Case
        if not root:
            return None

        queue=deque()
        queue.append(root)
        size=1# records the number of nodes shoule be deal with in current level

        while queue:
            formerNode=None
            for i in range(size):
                node=queue.popleft()
                if formerNode:
                    formerNode.next=node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                formerNode=node
            size=len(queue)

        return root




if __name__ == '__main__':
    solution=Solution()
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    node5=Node(5)
    node6=Node(7)

    node1.left=node2
    node1.right=node3
    node2.left=node4
    node2.right=node5
    node3.right=node6
    print(solution.connect(node1))
