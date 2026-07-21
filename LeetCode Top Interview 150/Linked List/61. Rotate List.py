# Definition for singly-linked list.
from logging import lastResort
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #T=O(n), S=O(1)
        if not head:
            return None
        cur=head
        n=0#len of ListNode
        while cur:#calculate the length of the ListNode
            cur=cur.next
            n+=1
        k=k%n #k mod n to avoid unnecessary operations
        if k==0:
            return head
        cur=head
        for _ in range(n-k-1):
            cur=cur.next
        #now we find the previous node before the node we rotate
        tailNode=cur#denotes the last node after rotation
        headNode=cur.next#denotes the head node after notation
        while cur.next:
            cur=cur.next
        #now the cur node is the last node of the LinkedList
        cur.next=head
        tailNode.next=None
        return headNode







if __name__ == '__main__':
    solution=Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print(solution.rotateRight(node1,0))
