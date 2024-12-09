# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head=ListNode()
        dummy_head.next=head
        f=s=dummy_head
        while(n>0):
            n-=1
            f=f.next
        while(f.next):
            f=f.next
            s=s.next
        s.next=s.next.next
        return dummy_head.next






if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    solution=Solution()
    solution.removeNthFromEnd(node1,2)