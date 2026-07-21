from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next:None, random:None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited={}#to map the old_node with new_node

    def getCloneNode(self,node):
        if node:
            if node not in self.visited:
                new_node=Node(node.val,None,None)#create a new node
                self.visited[node]=new_node#map the old node with new node
                return self.visited[node]
            else:#the old node already in visited
                return self.visited[node]#return the new node
        return None

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return head

        old_node=head
        new_node=Node(old_node.val,None,None)
        self.visited[old_node]=new_node

        while old_node:
            new_node.random=self.getCloneNode(old_node.random)
            new_node.next=self.getCloneNode(old_node.next)

            new_node=new_node.next
            old_node=old_node.next
        return self.visited[head]#return the map of the head of the old node






if __name__ == '__main__':
    solution=Solution()
    print(solution.copyRandomList())
