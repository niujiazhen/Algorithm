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
    #we use the level order to connect each node's next pointer to its next right node
    # T=O(n), S=O(n)
        if not root:
            return None
        queue=deque()
        queue.append(root)
        size=1#record the number of nodes we should handle of current level
        while queue:
            current_level_node=[]
            for i in range(size):
                node=queue.popleft()
                # current_level_node.append(node)# we don't need this, and we can optimize like the following
                if i<size-1:
                    node.next=queue[0]#the first element of queue is the right next node of current node
                else:
                    node.next=None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            #now we get the node of current level, and then we connect each node to its next right node
            # for i in range(len(current_level_node)):
            #     if i<len(current_level_node)-1:
            #         current_level_node[i].next=current_level_node[i+1]
            #     else:
            #         current_level_node[i]=None

            #but we can optimize this loop

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
