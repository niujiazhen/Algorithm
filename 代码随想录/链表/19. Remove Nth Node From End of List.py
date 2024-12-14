# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head=ListNode(next=head)
        l=r=dummy_head
        for i in range(n):
            r=r.next
        while(r.next):
            l=l.next
            r=r.next
        l.next=l.next.next
        return dummy_head.next




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
    node4.next=node5
    solution.removeNthFromEnd(node1,2)
